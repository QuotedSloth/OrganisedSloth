from database.connection import initialise_database


def main():
    initialise_database()
    print("Shared Planner starting...")


if __name__ == "__main__":
    main()