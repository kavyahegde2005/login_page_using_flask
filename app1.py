from flask import Flask,render_template,url_for,redirect

app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome to the Dino-chat'

@app.route('/login')
def login_page():
    return render_template('index.html')

@app.route('/admin')
def welcome_page():
    return 'Login Successful'

@app.route('/guest')
def guest_page():
    return 'Login Failed, Try again!'

@app.route('/user/<name>')
def user(name):
    if name == 'Kavya':
        return redirect(url_for('welcome_page'))
    else:
        return redirect(url_for('guest_page'))

if __name__ == '__main__':
    app.run(debug=True,port=2000)