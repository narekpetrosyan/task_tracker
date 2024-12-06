from .user import get_user_by_email


def query_tasks():
    email = input("Enter email if the user: ")
    user = get_user_by_email(email=email)
    if not user:
        print("There was no user with that email")
        return

    for task in user.tasks:
        print(
            f"Task ID: {task.id}, Title: {task.title}, Description: {task.description} \n"
        )
