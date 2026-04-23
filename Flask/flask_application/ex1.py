from flask import Flask
app=Flask(__name__)

@app.route("/")
def home():
    return "Welcome "

@app.route("/greet1")
def greet1():
    return "Greet1 Welcome  "

@app.route("/greet2")
def greet2():
    return "Greet2 Welcome  "
@app.route("/greet1/greet2")
def greet12():
    return "Greet12 Welcome "
if __name__== "__main__":
    app.run(debug=True)
home()
