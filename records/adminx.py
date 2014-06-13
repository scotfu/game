import xadmin
from xadmin import views
from models import Record,Group,Parameter
from xadmin.layout import Main, TabHolder, Tab, Fieldset, Row, Col, AppendedText, Side
from xadmin.plugins.inline import Inline
from xadmin.plugins.batch import BatchChangeAction



class RecordAdmin(object):
    
    list_display = ('id', 'player', 'result','g_round','group','time_seconds')

    
    search_fields = ['name']
    relfield_style = 'fk-ajax'


class GroupAdmin(object):
    list_display = ('id','name','num_of_players','time_seconds')

class ParameterAdmin(object):
    list_display = ('id','name','value')
    

    

xadmin.site.register(Record, RecordAdmin)
xadmin.site.register(Group, GroupAdmin)
xadmin.site.register(Parameter, ParameterAdmin)
