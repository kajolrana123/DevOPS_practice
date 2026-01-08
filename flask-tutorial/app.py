from flask import Flask, request, render_template
from datetime import datetime

app = Flask(__name__)

# just a home page message

@app.route('/')
def home():

    day_of_week = datetime.today().strftime('%A')
    current_time = datetime.now().strftime('%H:%M:%S')

    return render_template('index.html', day_of_week = day_of_week, current_time = current_time)

# adding a second page in the web
@app.route('/second')
def second():
    return "welcome to second web page "

# adding a page with user input 'name'
# use input will be showing in the console
@app.route('/api/<name>')
def name(name):
    return "welcome to api "

# adding a page with user input 'name' and return a message in the webpage
@app.route('/web/<name>')
def web(name):
    length = len(name)
    result = "Hello " + name + " !"

    if length >= 6:
        return "Name is too long "
    else:
        return "Nice name  " + result

# Basic add function
@app.route('/add/<a>/<b>')
def add(a,b):
    add = int(a) + int(b)

    result = {
        ' ans ' : add
    }

    return 'added ' + a + ' and '+ b +  ' = ' + str(result)

# adding an application page to show the name and age of user input
@app.route('/application')
def application():

    name = request.values.get('name')
    age  = request.values.get('age')

    data = {
        'age'  : age,
        'name' : name
    }

    return data

if __name__ == '__main__':
    app.run(debug=True)