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

EXAMPLE2=[  ('0','root2','',['2_1','2_2']),
            ('2_1','gatti2','gatti2',['2_11','2_12']),
            ('2_11','kitty2','gatti2 > kitty2',['2_111']),
            ('2_12','zoe2','gatti2 > zoe2',['2_121']),
            ('2_111','cip2','gatti2 > kitty2 > cip2',[]),
            ('2_121','kiky2','gatti2 > zoe2 > kitty2',[]),
            ('2_2','tazze2','tazze2',['2_21','2_22','2_23']),
            ('2_21','tazza2 21','tazze2 > tazza2 21',[]),
            ('2_22','tazze2 22','tazze2 > tazza2 22',[]),
            ('2_23','tazze2 23','tazze2 > tazza2 23',[]),
          ]


class Sources(object):
    implements(ISources)

    sources = dict()

    def __init__(self, context):
        self.context = context
        self.sources['my.vocabolary.source']=Source(EXAMPLE)
        self.sources['my.vocabolary.source2']=Source(EXAMPLE2)

class Source(object):
    implements(ISource)

    def __init__(self,my_tree):
        self.my_tree=my_tree

    def get_info(self,node_id):
        for id,label,full_label,children in self.my_tree:
            if node_id==id:
                return dict(id=id,label=label,full_label=full_label)
        return dict(id='',label='',full_label='')


    def get_children(self,node_id):
        for id,label,full_label,children in self.my_tree:
            if node_id==id:
                return [dict(id=id,label=label,full_label=full_label) for id,label,full_label,c_children in self.my_tree if id in children]

        return []

    def search(self,text):
        return [dict(id=id,label=label,full_label=full_label) for id,label,full_label,children in self.my_tree if text in full_label]

