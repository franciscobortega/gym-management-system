"""Models for Cadence app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    """A user."""

    __tablename__ = 'users'

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    role = db.Column(db.Enum('admin', 'staff', 'member'), nullable=False)
    phone = db.Column(db.String)

    members = db.relationship("Member", back_populates="user")
    staff = db.relationship("Staff", back_populates="user")

class Member(db.Model):
    """A member."""

    __tablename__ = 'members'

    member_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    date_of_birth = db.Column(db.Date)
    address = db.Column(db.String)
    start_date = db.Column(db.Date, nullable=False)
    membership_plan = db.Column(db.Integer, db.ForeignKey('memberships.membership_id'))
    status = db.Column(db.Enum('active', 'expired'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    
    user = db.relationship("User", back_populates="members")
    payments = db.relationship("Payment", back_populates="member")

class Staff(db.Model):
    """A staff person."""

    __tablename__ = 'staff'

    staff_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    date_of_birth = db.Column(db.Date)
    position = db.Column(db.String)
    email = db.Column(db.String)
    phone = db.Column(db.String)
    hire_date = db.Column(db.Date)
    salary = db.Column(db.Float)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    
    user = db.relationship("User", back_populates="staff")

class Equipment(db.Model):
    """A piece of equipment."""
    
    __tablename__ = 'equipment'

    equipment_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.Text)
    purchase_date = db.Column(db.Date)
    status = db.Column(db.Enum('in service', 'out of service'), nullable=False)
    last_maintenance = db.Column(db.Date)

class Membership(db.Model):
    """A membership plan."""
    
    __tablename__ = 'memberships'

    membership_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    plan_name = db.Column(db.String, nullable=False)
    description = db.Column(db.Text)
    price = db.Column(db.Float, nullable=False)
    duration = db.Column(db.Integer, nullable=False)
    features = db.Column(db.Text)

class Payment(db.Model):
    """A payment."""
    
    __tablename__ = 'payments'

    payment_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    member_id = db.Column(db.Integer, db.ForeignKey('members.member_id'))
    payment_date = db.Column(db.Date, nullable=False)
    amount = db.Column(db.Float, nullable=False)
    payment_method = db.Column(db.String)
    status = db.Column(db.Enum('completed', 'pending', 'rejected'), nullable=False)

    member = db.relationship("Member", back_populates="payments")


def connect_to_db(flask_app, db_uri="postgresql:///gym-management-system", echo=True):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the database!")


if __name__ == "__main__":
    from server import app

    # Call connect_to_db(app, echo=False) if your program output gets
    # too annoying; this will tell SQLAlchemy not to print out every
    # query it executes.

    connect_to_db(app)