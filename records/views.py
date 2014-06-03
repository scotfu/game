import json

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.db.models import Count
from django.views.decorators.csrf import csrf_exempt
from .models import Record

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
@csrf_exempt
def result(request):
    if request.method =='POST':
        result = request.POST.get('result',None)
        player = request.POST.get('player',None)
        try:
            Record.objects.create(result=result,player=player)
        except Exception as e:
            return {'result':'false','msg':e}    
        return {'result':'true'}
    else:
        return {'result':'false','msg':'Please use POST'}