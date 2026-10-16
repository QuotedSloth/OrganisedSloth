from database.connection import get_connection

def create_user(username, password_hash):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""INSERT INTO users (username , password_hash) VALUES (?, ?)""", (username, password_hash))

    connection.commit()
    connection.close()

def get_user(username):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""SELECT user_id, username, password_hash FROM  users WHERE  username = ?""", (username,))
    user = cursor.fetchone()

    connection.close()
    return user

def get_all_users():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT user_id, username, password_hash
        FROM users
    """)

    users = cursor.fetchall()

    connection.close()
    return users

def create_project(project_name, owner_id):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""INSERT INTO projects (project_name, owner_id) VALUES (?, ?)""", (project_name, owner_id))

    connection.commit()
    connection.close()

def get_user_projects(user_id):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""SELECT project_id, project_name FROM projects WHERE owner_id = ?""", (user_id,))
    projects = cursor.fetchall()

    connection.close()
    return projects