from flaskapp import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(20), nullable=False)                                   


    def __repr__(self):
        return f"User('{self.username}')"


class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Day = db.Column(db.String(1), nullable=False)
    Time = db.Column(db.String(5), nullable=False)
    Name = db.Column(db.String(10), nullable=False)
    
    def __repr__(self):
        return f"User('{self.Day}','{self.Time}','{self.Name}')"