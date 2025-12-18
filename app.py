from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def name():
    return "Hello guys, to explore the site please login to our website!"

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        
        if username == "Kavya Hegde" and password == "2325":
            return redirect(url_for("dashboard"))
        else:
            return "Invalid credentials, try again!"

    return render_template("login.html")

@app.route("/dashboard")
def dashboard():
    return "Welcome to your dashboard!"

if __name__ == "__main__":
    app.run(debug=True, port=4000)
 
