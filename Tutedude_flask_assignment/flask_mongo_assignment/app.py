# 2. Create a form on the frontend that, when submitted,
# inserts data into MongoDB Atlas. Upon successful submission,
# the user should be redirected to another page displaying
# the message "Data submitted successfully".
# If there's an error during submission, display the error on
# the same page without redirection.

from flask import Flask, request, render_template, redirect, url_for
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB
uri = "mongodb+srv://kajolrana123_db_user:uPP3LdSw2TezPEF8@kajol.0rgp2xj.mongodb.net/?appName=Kajol"
client = MongoClient(uri)

db = client["assignment_db"]
collection = db["users"]

@app.route('/', methods=['GET', 'POST'])
def form():
    error = None

    if request.method == 'POST':
        name = request.form.get('name')
        password = request.form.get('password')

        if not name or not password:
            error = "All fields are required"
        else:
            try:
                collection.insert_one({
                    "name": name,
                    "password": password
                })
                # Redirect on success
                return redirect(url_for('success'))
            except Exception as e:
                # Show error on same page
                error = str(e)

    return render_template('form.html', error=error)

@app.route('/success')
def success():
    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True)
