from Products.Five import BrowserView
import simplejson as json

from abstract.widgets.multitree.widget import MultiTreeWidget
from abstract.widgets.multitree.interfaces import ISources

class MultiTreeJSONView(BrowserView):

    def _get_source(self,fieldName=''):
        source=None
        sources=ISources(self.context)

        fieldName=self.request.get('field_name',fieldName)
        if len(fieldName)>0:
            schema=self.context.Schema()
            field=schema.get(fieldName)
            if field is not None:
                widget = field.widget
                source_label = getattr(widget,'source','')
                if len(source_label)>0:
                    source=sources.sources[source_label]
        return source

    def plain_subtree(self):
        self.request.response.setHeader("Content-type","application/json")
        result_list=[]

        qry=self.request['q']
        source=self._get_source()
        if source is not None:
            result_list=[dict(id=row['id'],name=row['full_label']) for row in source.search(qry)]

        return json.dumps(result_list)

    def structured_subtree(self):
        self.request.response.setHeader("Content-type","application/json")
        result_list=[]

        qry=self.request.get('id','')
        source=self._get_source()
        if source is not None:
            result_list=[dict(data=row['label'],state='closed',attr={'id':row['id'],}) for row in source.get_children(qry)]


        return json.dumps(result_list)

    def convert_values(self,fieldName,values):
        result_list=[]
        source=self._get_source(fieldName=fieldName)
        if source is not None:
            for id in values:
                result_list.append(source.get_info(id))
        return result_list

    def get_info(self):
        self.request.response.setHeader("Content-type","application/json")
        result_obj=[]
        source=self._get_source()
        if source is not None:
            id=self.request.get('id',None)
            if id is not None:
                result_obj=source.get_info(id)

        return json.dumps(result_obj)


