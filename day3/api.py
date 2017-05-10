import requests                                     
import json                                         

api_key = "a4338eb235334f70b746085f0882367f"  
base_url = "http://api.nytimes.com/svc/movies/v2/reviews,json"

def find_review(**kwargs):                          
  if 'apiKey' not in kwargs:                        
    kwargs['apiKey'] = api_key

  r = requests.get(base_url, params=kwargs)              
  return json.loads(r.text)                         


print find_review(title = "Sing")