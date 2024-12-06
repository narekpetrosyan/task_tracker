from src.models import Task
from src.config import session
from src.queries import get_user_by_email
from src.utils import confirm_action


def add_task():
    email = input("Enter email of the user: ")
    user = get_user_by_email(email=email)
    if not user:
        print("No user found with that email!")
        return

    title, description = input("Enter the title: "), input("Enter the description: ")
    session.add(Task(title=title, description=description, user=user))
    session.commit()
    print(f"\n\nAdded to the database: {title}:{description}\n\n")


def delete_task():
    task_id = input("Enter ID of the task: ")
    task = session.query(Task).get(task_id)
    if not task:
        print("No user found with that email!")
        return

    if confirm_action(f"Are you sure you want to delete: {task.id}?"):
        session.delete(task)
        session.commit()
        print("Task deleted!")
