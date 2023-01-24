from database import DataBase

class _UserTable:
    def create_table(self):
        db = DataBase().connect_to_database()
        cursor = db.cursor(buffered=True)
        sql_command = """CREATE TABLE IF NOT EXISTS users(
        id INTEGER AUTO_INCREMENT primary key,
        username VARCHAR(50),
        password VARCHAR(50),
        user_role VARCHAR(50)
        )"""
        cursor.execute(sql_command)
        db.commit()
        cursor.close()

class AddUser:
    def __init__(self, username, user_password, user_role):
        self.username = username
        self.user_password = user_password
        self.user_role = user_role

    def add_user(self):
        db = DataBase().connect_to_database()
        cursor = db.cursor(buffered=True)
        _UserTable().create_table()
        sql_command = "INSERT INTO users (username, password, user_role) VALUES (%s, %s, %s)"
        content = (self.username, self.user_password, self.user_role)
        cursor.execute(sql_command, content)
        db.commit()
        cursor.close()

class CurrentUser:
    def get_user(self, username):
        db = DataBase().connect_to_database()
        cursor = db.cursor(buffered=True)
        cursor.execute(f"SELECT * FROM users WHERE username = '{username}'" )
        user = cursor.fetchone()
        cursor.close()
        return user

    


