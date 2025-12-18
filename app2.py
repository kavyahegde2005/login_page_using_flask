from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to Student Portal"

@app.route('/home')
def page():
    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True,port=2500)