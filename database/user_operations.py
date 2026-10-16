from database.connection import get_connection

def create_user(username, password_hash):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO users (username, password_hash)
        VALUES (?, ?)
    """, (username, password_hash))

    connection.commit()
    connection.close()


def get_user(username):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT user_id, username, password_hash
        FROM users
        WHERE username = ?
    """, (username,))

    user = cursor.fetchone()

    connection.close()
    return user