"""CRUD operations."""

from model import db, User, Member, Staff, Equipment, Membership, Payment, connect_to_db


def create_user(username, email, password, role, phone):
    """Create and return a new user."""

    user = User(username=username, email=email, password=password, role=role, phone=phone)

    return user

def create_member(first_name, last_name, date_of_birth, address, start_date, membership_plan, status):
    """Create and return a new member."""

    member = Member(first_name=first_name, last_name=last_name, date_of_birth=date_of_birth, address=address, start_date=start_date, membership_plan=membership_plan, status=status)

    return member 

def create_staff(first_name, last_name, date_of_birth, position, email, phone, hire_date, salary):
    """Create and return a new staff member."""

    staff = Staff(first_name=first_name, last_name=last_name, date_of_birth=date_of_birth, position=position, email=email, phone=phone, hire_date=hire_date, salary=salary)

    return staff 

def create_equipment(name, description, purchase_date, status, last_maintenance):
    """Create and return a new piece of equipment."""

    equipment = Equipment(name=name, description=description, purchase_date=purchase_date, status=status, last_maintenance=last_maintenance)

    return equipment 

def create_membership(plan_name, description, price, duration, features):
    """Create and return a new membership plan."""

    membership = Membership(plan_name=plan_name, description=description, price=price, duration=duration, features=features)

    return membership 

def create_payment(payment_date, amount, payment_method, status):
    """Create and return a new payment."""

    payment = Payment(payment_date=payment_date, amount=amount, payment_method=payment_method, status=status)

    return payment 


if __name__ == '__main__':
    from server import app
    connect_to_db(app)