import requests,json

BASE_URL='http://127.0.0.1:8000/'
ENDPOINT='api/'
def get_records(id=None):
    dic={}
    if id is not None:
        dic={
            'id':id
        }
    resp=requests.get(BASE_URL+ENDPOINT,data=json.dumps(dic))
    print(resp.status_code)
    print(resp.json())
get_records(3)
