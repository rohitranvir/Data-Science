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
# get_records(3)
def create_record():
    new_data={
        'ename':'Rohit',
        'esal':18000,
        'eaddr':'At pusad',
        'eno':101
    }
    resp=requests.post(BASE_URL+ENDPOINT,data=json.dumps(new_data))
    print(resp.status_code)
    print(resp.json())
# create_record()
def update_record(id):
    new_emp={
        'id':id,
        'ename':'Rohit',
        'eno':502,
        'esal':18000,
        'eaddr':'nagpur'
        }
    resp=requests.put(BASE_URL+ENDPOINT,data=json.dumps(new_emp))
    print(resp.status_code)
    print(resp.json())
update_record(1)