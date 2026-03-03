from flask import Flask,request
app=Flask(__name__)
items=[
            {
                "name":"Green Apple mojito",
                "price":160
            },
            {
                "name":"momos",
                "price":160
            }
]


@app.get('/get-items')
def get_items():
    return {"items":items}


@app.post('/add-items')
def add_items():
    request_data=request.get_json()
    items.append(request_data)
    return {"message":"item added successfully"}