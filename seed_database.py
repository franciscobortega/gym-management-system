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


# --------------- Seed user --------------- #

# Create a new user using the create_user function
new_user = crud.create_user(
    username="johndoe",
    email="johndoe@email.com",
    password="1234",
    role="member",
    phone="123-456-7890"
)

# Create a new member using the create_member function
# new_member = crud.create_member(
#     first_name="John",
#     last_name="Doe",
#     date_of_birth=date(2000, 1, 1),
#     address="123 Main St",
#     start_date=date.today(),
#     membership_plan=1,  
#     status="active"
# )

# Associate the new member with the new user
# new_member.user = new_user

# Add both the user and member to the session and commit to the database
model.db.session.add(new_user)
# model.db.session.add(new_member)
model.db.session.commit()

