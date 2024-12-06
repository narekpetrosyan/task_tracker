from ..models import User
from ..config import session


def query_users():
    for user in session.query(User).all():
        print(f"ID: {user.id}, Name: {user.name}, Email: {user.email} \n")


def get_user_by_email(email):
    return session.query(User).filter_by(email=email).first()
