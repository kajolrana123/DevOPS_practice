from flask import Flask, request, render_template
from datetime import datetime
from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://kajolrana123_db_user:uPP3LdSw2TezPEF8@kajol.0rgp2xj.mongodb.net/?appName=Kajol"

client = MongoClient(uri)

try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

# Database & Collection
db = client["student_db"]
users_collection = db["users"]

app = Flask(__name__)

# Home / Signup page
@app.route('/', methods=['GET', 'POST'])
def home():
    day_of_week = datetime.today().strftime('%A')
    current_time = datetime.now().strftime('%H:%M:%S')

    message = None

    if request.method == 'POST':
        name = request.form.get('name')
        password = request.form.get('password')

        if name and password:
            users_collection.insert_one({
                "name": name,
                "password": password
            })
            message = "User registered successfully!"
        else:
            message = "Please fill all fields"

    return render_template(
        'index.html',
        day_of_week=day_of_week,
        current_time=current_time,
        # message=message
    )

if __name__ == '__main__':
    app.run(debug=True)
