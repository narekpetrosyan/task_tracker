from src.models import User
from src.config import session
from src.utils import confirm_action
from sqlalchemy.exc import IntegrityError
from src.queries import get_user_by_email


def add_user():
    name, email = input("Enter name: "), input("Enter email: ")
    if get_user_by_email(email):
        print(f"User already exists: {email}")
        return

    try:
        session.add(User(name=name, email=email))
        session.commit()
        print(f"User {name} added.")
    except IntegrityError:
        session.rollback()
        print("Error")


def update_user():
    email = input("Enter email who you want to update: ")
    user = get_user_by_email(email)
    if not user:
        print("No user found with that email!")
        return

    user.name = input("Enter new name (blank for same): ") or user.name
    user.email = input("Enter new email (blank for same): ") or user.email
    session.commit()
    print("User has been updated!")


def delete_user():
    email = input("Enter email who you want to delete: ")
    user = get_user_by_email(email)
    if not user:
        print("No user found with that email!")
        return

    if confirm_action(f"Are you sure you want to delete: {user.email}?"):
        session.delete(user)
        session.commit()
        print("User deleted!")
