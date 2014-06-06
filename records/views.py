import json

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse,Http404
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.db.models import Count
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q

from .models import Record,Group

@csrf_exempt
def json_response(func):
    """
    A decorator thats takes a view response and turns it
    into json. If a callback is added through GET or POST
    the response is JSONP.
    """
    def decorator(request, *args, **kwargs):
        objects = func(request, *args, **kwargs)
        if isinstance(objects, HttpResponse):
            return objects
        try:
            data = json.dumps(objects)
            if 'callback' in request.REQUEST:
                # a jsonp response!
                data = '%s(%s);' % (request.REQUEST['callback'], data)
                return HttpResponse(data, "text/javascript")
        except Exception as e:
            print e
            data = json.dumps(str(objects))
        return HttpResponse(data, "application/json")
    return decorator

@json_response
def push(request):
    if request.method =='POST':
        result = request.POST.get('result',None)
        player = request.POST.get('player',None)
        group_id = request.session.get('group_id',None)
        g_round = request.session.get('g_round',1)
        try:
            group = Group.objects.get(id=group_id)
            Record.objects.create(result=result, player=player, group=group, g_round=g_round)
        except Exception as e:
            return {'result':'false','msg':e}    
        return {'result':'true'}
    else:
        return {'result':'false','msg':'Please use POST'}


@json_response
def pull(request):
    if request.method =='GET':
        group_id = request.session.get('group_id',None)
        player = request.GET.get('player',None)
        g_round = request.GET.get('g_round',None)
        
        data = {}
        data['records']=[]
        while not data['records']:
            try:
                group = Group.objects.get(id=group_id)
                records = Record.objects.filter(~Q(player=player),group=group, g_round=1)
            except Exception as e:
                return {'result':'false','msg':e}
            for record in records:
                    data['records'].append(
                                  {'player':record.player,
                                   'result':record.result,})
        return data
    else:
        return {'result':'false','msg':'Please use GET'}


def render_game(request):
    request.session.set_expiry(0)
    if request.method =='GET':
        group_id = request.session.get('group_id', False)
        player = request.session.get('player', False)
        g_round = request.session.get('g_round', 1)
        if not (group_id and player):
            try:
                group = Group.objects.all().order_by('id').reverse()[0]
                print group,group.num_of_players
                if group.num_of_players >= 2:
                    raise Exception,'The group is full'
            except Exception as e:
                print e,'I just created a new group'
                group = Group.objects.create(name="my test", num_of_players=0)
            group.num_of_players = group.num_of_players + 1
            group_id = group.id
            player = "Player " + str(group.num_of_players)
            group.save()
            request.session['group_id'] = group.id
            request.session['player'] = player
        return render_to_response('index.html', {
                                  'group_id': group_id,
                                  'player':player,
                                  'g_round':g_round},
                                  context_instance=RequestContext(request))
    else:
        return Http404