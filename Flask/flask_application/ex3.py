from flask import Flask,redirect,url_for
app=Flask(__name__)

@app.route("/")
def home():
    return "Welcome "


@app.route("/add/<int:a>/<int:b>")
def add(a,b):
    return str(a+b)


if __name__== "__main__":
    app.run(debug=True)
home()
