import sqlite3
from pathlib import Path


DATABASE = Path(__file__).parent / "planner.db"
SCHEMA = Path(__file__).parent / "schema.sql"


def get_connection():
    return sqlite3.connect(DATABASE)


def initialise_database():
    connection = get_connection()

    with open(SCHEMA, "r") as file:
        schema = file.read()

    connection.executescript(schema)
    connection.commit()
    connection.close()