from src.models import Base
from src.config import engine
from src.transactions import add_task, add_user, update_user, delete_task, delete_user
from src.queries import query_tasks, query_users


Base.metadata.create_all(engine)


def main():
    actions = {
        "1": add_user,
        "2": add_task,
        "3": query_users,
        "4": query_tasks,
        "5": update_user,
        "6": delete_user,
        "7": delete_task,
    }

    while True:
        print(
            "Options: \n 1. Add user\n 2. Add task \n 3. Query users \n 4. Query tasks \n 5. Update user \n 6. Delete user \n 7. Delete task \n 8. Exit \n"
        )
        choice = input("Enter an option: ")
        if choice == "8":
            print("Bye")
            break
        action = actions.get(choice)
        if action:
            action()
        else:
            print("\n\nNot a choice! \n\n")


if __name__ == "__main__":
    main()
