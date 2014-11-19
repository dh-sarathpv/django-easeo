'''
Created on 16-Oct-2014

@author: sarath
'''
from django.http.response import HttpResponse
from google.appengine.api import urlfetch
import logging
class EaSeoMiddleWare:
    
    def process_request(self, request):
        
        try:
            if request.GET['_escaped_fragment_']!='':
                
                location = request.get_full_path()
                absolute_uri = request.build_absolute_uri(location)
                try:
                    resp = urlfetch.fetch('http://2.angular-seo-dev-1001.appspot.com/service/v1/snapshot?url='+absolute_uri, method=urlfetch.GET, deadline=300)
                    
                    content = resp.content
                    logging.debug(content)
                    return HttpResponse(content)
                except urlfetch.DownloadError:
                    pass

        
        except:
            pass    