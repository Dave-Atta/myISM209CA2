from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'users'
    first_name = db.Column(db.String(20), unique = False, nullable = False)
    surname = db.Column(db.String(20), unique = False, nullable = False)
    date_of_birth = db.Column(db.String(20), unique = False, nullable = False)
    residential_address = db.Column(db.Text, unique = False, nullable = False)
    nationality = db.Column(db.String, unique = False, nullable = False)
    national_identification_number = db.Column(db.Integer(20), primary_key=True)


def __repr__(self):
    return '<User {}>'.format(self.id)
