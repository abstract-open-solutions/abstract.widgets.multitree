from Products.Five import BrowserView
import json

from abstract.widgets.multitree.widget import MultiTreeWidget
from abstract.widgets.multitree.interfaces import ISources

class MultiTreeJSONView(BrowserView):

    def _get_source(self,sourceName=''):
        source=None
        sources=ISources(self.context)
        if len(sourceName)>0:
            try:
                source=sources.sources[sourceName]
            except KeyError:
                pass
        return source

    def _get_sources_from_field(self,fieldName):
        sources_available=[]
        sources=ISources(self.context)
        schema=self.context.Schema()
        field=schema.get(fieldName)
        widget = field.widget
        for (source,source_label) in getattr(widget,'sources',[]):
            try:
                sources_available.append(sources.sources[source])
            except KeyError:
                continue
        return sources_available

    def _find_in_sources(self, id, sources):
        found=None
        for source in sources:
            info=source.get_info(id)
            if info.get('id',None)==id:
                found=info
                break
        return found

    def plain_subtree(self):
        self.request.response.setHeader("Content-type","application/json")
        result_list=[]
        qry=self.request['q']
        source=self._get_source(self.request.get('source_name',''))
        if source is not None:
            result_list=[dict(id=row['id'],name=row['full_label']) for row in source.search(qry)]
        return json.dumps(result_list)

    def structured_subtree(self):
        self.request.response.setHeader("Content-type","application/json")
        result_list=[]
        qry=self.request.get('id','')
        source=self._get_source(self.request.get('source_name',''))
        if source is not None:
            for row in source.get_children(qry):
                child_desc=dict(data=row['label'],attr={'id':row['id'],})
                if len(source.get_children(row['id'])):
                    child_desc['state']='closed'
                result_list.append(child_desc)
        return json.dumps(result_list)

    def convert_values(self,fieldName,values):
        #from field get all sources
        sources=self._get_sources_from_field(fieldName)

        #for all value search a value in every source
        result_list=[]
        for value in values:
            info=self._find_in_sources(value,sources)
            if info is not None:
                result_list.append(info)

        return result_list

    def get_info(self):
        self.request.response.setHeader("Content-type","application/json")
        result_obj=[]
        source=self._get_source(self.request.get('source_name',''))
        if source is not None:
            id=self.request.get('id',None)
            if id is not None:
                result_obj=source.get_info(id)
        return json.dumps(result_obj)
