from Products.Five import BrowserView
import simplejson as json

class MultiTreeJSONView(BrowserView):
  
    def _get_data(self,qry):
        alls=[{"id":"10","name":"pippo"},
             {"id":"20","name":"kitty"},
             {"id":"30","name":"zoe"},
             {"id":"40","name":"pippa"}]
        
        res=[]
        for row in alls:
            if qry in row['name']:
                res.append(row)

        return res
    
    def __call__(self):
        self.request.response.setHeader("Content-type","application/json")
        
        result_list=self._get_data(self.request['q'])
        
        return json.dumps(result_list)
        


