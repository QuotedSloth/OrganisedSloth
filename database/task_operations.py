from database.connection import get_connection

def create_task(project_id, title, description, due_date, priority, created_by, assigned_to):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO tasks (
            project_id,
            title,
            description,
            due_date,
            priority,
            created_by,
            assigned_to
        )
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        project_id,
        title,
        description,
        due_date,
        priority,
        created_by,
        assigned_to
    ))

    connection.commit()
    connection.close()

def get_project_tasks(project_id):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT task_id, title, description, due_date, priority,
               status, created_by, assigned_to
        FROM tasks
        WHERE project_id = ?
    """, (project_id,))

    tasks = cursor.fetchall()

    connection.close()
    return tasks

def update_task(task_id, title, description, due_date, priority, status, assigned_to):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        UPDATE tasks
        SET title = ?,
            description = ?,
            due_date = ?,
            priority = ?,
            status = ?,
            assigned_to = ?
        WHERE task_id = ?
    """, (
        title,
        description,
        due_date,
        priority,
        status,
        assigned_to,
        task_id
    ))

    connection.commit()
    connection.close()