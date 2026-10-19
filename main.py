from database.connection import initialise_database
from task.operations import update_task


def main():
    initialise_database()
    print("Shared Planner starting...")


if __name__ == "__main__":
    main()