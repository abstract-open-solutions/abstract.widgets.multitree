from zope.interface import implements

from interfaces import ISources,ISource

from plone.registry.field import DottedName, Dict



EXAMPLE=[   ('0','root','',['1','2']),
            ('1','gatti','gatti',['11','12']),
            ('11','kitty','gatti > kitty',['111']),
            ('12','zoe','gatti > zoe',['121']),
            ('111','cip','gatti > kitty > cip',[]),
            ('121','kiky','gatti > zoe > kitty',[]),
            ('2','tazze','tazze',['21','22','23']),
            ('21','tazza 21','tazze > tazza 21',[]),
            ('22','tazze 22','tazze > tazza 22',[]),
            ('23','tazze 23','tazze > tazza 23',[]),
          ]

class Sources(object):
    implements(ISources)

    sources = dict()

    def __init__(self, context):
        self.context = context
        self.sources['my.vocabolary.source']=Source()
        

class Source(object):
    implements(ISource)
    
    def get_info(self,node_id):
        for id,label,full_label,children in EXAMPLE:
            if node_id==id:
                return dict(id=id,label=label,full_label=full_label)
        return dict(id='',label='',full_label='')
        
    
    def get_children(self,node_id):
        for id,label,full_label,children in EXAMPLE:
            if node_id==id:
                return [dict(id=id,label=label,full_label=full_label) for id,label,full_label,c_children in EXAMPLE if id in children]
            
        return []
       
    def search(self,text):
        return [dict(id=id,label=label,full_label=full_label) for id,label,full_label,children in EXAMPLE if text in full_label]

