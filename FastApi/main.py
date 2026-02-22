from fastapi import FastAPI,Path,HTTPException,Query
# The Path() function in FastAPI is used to provide metadata, validation
# rules, and documentation hints for path parameters in your API
# endpoints.
# Title
# Description
# Example
# ge, gt, le, It
# Min_length
# Max_length
# regex
import json 
app=FastAPI()
def load_data():
    with open('patient.json','r') as f:
        data=json.load(f)
    return data
@app.get("/")
def hello():
    return {"message":"Patient Management Api"}
@app.get("/about")
def about():
    return {"message":"A fully functional api to manage your patient record"}
@app.get('/view')
def view():
    data=load_data()
    return data
@app.get('/patient/{patient_id}')
def view_patient(patient_id:str=Path(...,description="Id of an patient in the DB",example='P001')):
    # Load all the patient
    data=load_data()
    if patient_id in data:
        return data[patient_id]
    # return {'error':'patient not found'}
    raise HTTPException(status_code=404,detail='patient not found')
@app.get('/sort')
def sort_patient(sort_by :str=Query(...,description="Sort on the basis on BMI "),order:str=Query('asc',description='Sort in ascending or descending or descending order')):
    valid_field=['height','weight', 'bmi']
    if sort_by not in valid_field:
        raise HTTPException(status_code=400,detail='Invalid field Select from valid Fields{valid_field}')
    if order not in ['asc','desc']:
        raise HTTPException(status_code=400,detail='Invalid order Select from valid order{order}')
    data=load_data()
    sort_order = False if order =='asc' else  True
    sorted_data=sorted(data.values(),key=lambda x:x[sort_by],reverse=sort_order)
    return sorted_data
    
