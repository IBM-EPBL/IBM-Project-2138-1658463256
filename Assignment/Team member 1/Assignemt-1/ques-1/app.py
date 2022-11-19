from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__,template_folder='templates')

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods=["POST","GET"])
def login(): 
    if request.method =="POST":
        nm = request.form.get("nm")
        email= request.form.get("email")
        num = request.form.get("num")
        return nm + email + num
    else:
        return render_template("login.html")
   


if __name__ == "__main__":
    app.run(debug=True)

