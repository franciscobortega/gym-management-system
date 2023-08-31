"""Script to seed database."""

import os
import json
from datetime import date

import crud
import model
import server

os.system("dropdb gym")
os.system('createdb gym')

model.connect_to_db(server.app)
model.db.create_all()


# --------------- Seed memberships --------------- #
membership_1 = crud.create_membership(
    plan_name="Basic",
    description="Basic membership plan",
    price=10.0,
    duration=30,
    features="Basic access to gym facilities"
)

membership_2 = crud.create_membership(
    plan_name="Premium",
    description="Premium membership plan",
    price=30.0,
    duration=30,
    features="Basic access to gym facilities + access to all classes"
)

model.db.session.add(membership_1)
model.db.session.add(membership_2)
model.db.session.commit()


# --------------- Seed equipment --------------- #
equipment_1 = crud.create_equipment(
    name="Treadmill",
    description="A device used for walking or running.",
    purchase_date=date(2020, 1, 1),
    status="in service",
    last_maintenance=date(2020, 1, 1)
)

equipment_2 = crud.create_equipment(
    name="Squat Rack",
    description="A piece of weight training equipment.",
    purchase_date=date(2020, 1, 1),
    status="out of service",
    last_maintenance=date(2023, 1, 1)
)

model.db.session.add(equipment_1)
model.db.session.add(equipment_2)
model.db.session.commit()


# --------------- Seed user --------------- #
# Create a new user using the create_user function
new_user = crud.create_user(
    username="johndoe",
    email="johndoe@email.com",
    password="1234",
    role="member",
    phone="123-456-7890"
)


# --------------- Seed member --------------- #
# Create a new member using the create_member function
new_member = crud.create_member(
    first_name="John",
    last_name="Doe",
    date_of_birth=date(2000, 1, 1),
    address="123 Main St",
    start_date=date.today(),
    membership_plan=1,  
    status="active"
)

# Associate the new member with the new user
new_member.user = new_user

# Add both the user and member to the session and commit to the database
model.db.session.add(new_user)
model.db.session.add(new_member)
model.db.session.commit()


# --------------- Seed staff --------------- #
# Create a new staff member using the create_staff function
new_staff = crud.create_staff(
    first_name="Jane",
    last_name="Doe",
    date_of_birth=date(2000, 1, 1),
    position="Manager",
    email="janedoe@gym.com",
    phone="123-456-7890",
    hire_date=date.today(),
    salary=50000.00
)

model.db.session.add(new_staff)
model.db.session.commit()


# --------------- Seed payment --------------- #
# Create a new payment using the create_payment function
new_payment = crud.create_payment(
    payment_date=date.today(),
    amount=10.00,
    payment_method="credit card",
    status="completed"
)

# Associate the new payment with the new member
new_payment.member = new_member

# Add the payment to the session and commit to the database
model.db.session.add(new_payment)
model.db.session.commit()