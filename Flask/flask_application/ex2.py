from flask import Flask,redirect,url_for
app=Flask(__name__)

@app.route("/")
def home():
    return "Welcome "

@app.route("/greet1")
def greet1():
    return (redirect("https://www.amazon.com/"))

@app.route("/greet2")
def greet2():
    return (redirect(url_for('greet1')))
@app.route("/greet1/greet2")
def greet12():
    return "Greet12 Welcome "
if __name__== "__main__":
    app.run(debug=True)
home()
