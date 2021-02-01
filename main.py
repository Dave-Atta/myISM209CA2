from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__) # create a flask app named app

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:bookexampledbpassword@localhost:5433/ bookexample'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

import models

@app.route("/")
def home():
    return 'My name is Feranmi Atta. This is my CA2 work. ' \
           'My GitHub URL is https://github.com/DaveTinsley'
    # In the return statement above, Use your own name and GitHub URL


@app.route("/register" , methods=['POST','GET'])
def register():
    return render_template('register.html')


first_name = request.form['first_name']
surname = request.form['surname']
date_of_birth = request.form['date_of_birth']
residential_address = request.form['residential_address']
nationality = request.form['nationality']
national_identification_number = request.form['national_identification_number']

try:
    user = models.User(first_name = first_name, surname = surname, date_of_birth = date_of_birth,
                       residential_address = residential_address, nationality = nationality, national_identification_number = national_identification_number)
    models.db.session.add(user)
    models.db.session.commit()

except Exception as e:
    error = 'Could not submit. The error message is {}'.format(e.__cause__)


if __name__ == "__main__":
    app.run(port=5005)
