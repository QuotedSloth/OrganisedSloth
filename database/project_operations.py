from database.connection import get_connection

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