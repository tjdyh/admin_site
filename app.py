from flask import Flask, request, make_response, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')
    # response = make_response('<h1>This document carries a cookie!</h1>')
    # response.set_cookie('answer', '42')
    # return response

@app.route('/hello')
def hello_world():
    user_agent = request.headers.get('User-Agent')
    return '<p>Your browser is {}</p>'.format(user_agent)

@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, {}!</h1>'.format(name)

# if __name__ == '__main__':
#     app.run()
