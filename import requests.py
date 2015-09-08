import requests
import json

query_params = {'access_token': '036f964f4fc6e4cce3d3586d4f23d81c9417ca91'#,
                #'login' : 'allak480098'
                #"longUrl" : 'http://google.com/'
                } 

#endpoint = 'https://api-ssl.bitly.com/v3/shorten/'
endpoint = 'https://api-ssl.bitly.com/v3/user/link_history'
response = requests.get(endpoint, params=query_params, verify=False)

data = json.loads(response.content)
#d2 = data[u'data']
#print d2[u'url']
print data