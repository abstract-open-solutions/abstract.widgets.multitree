from Products.Five import BrowserView
import simplejson as json

from abstract.widgets.multitree.widget import MultiTreeWidget

class MultiTreeJSONView(BrowserView):
  
    def _get_data(self,qry,alls):
        res=[dict(id=k,name=v) for k,v in alls.items() if qry in v]
        return res
    
    def __call__(self):
        self.request.response.setHeader("Content-type","application/json")
        result_list=[]
        
        qry=self.request['q']
        fieldName=self.request.get('field_name','')
        if len(fieldName)>0:
            schema=self.context.Schema()
            field=schema.get(fieldName)
            if field is not None:
                vocab = field.vocabulary
                result_list=self._get_data(qry,vocab)
        return json.dumps(result_list)
        


