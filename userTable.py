from database import DataBase

class _UserTable:
    def create_table(self):
        db = DataBase().connect_to_database()
        cursor = db.cursor(buffered=True)
        sql_command = """CREATE TABLE IF NOT EXISTS users(
        id INTEGER AUTO_INCREMENT primary key,
        username VARCHAR(50) ,
        password VARCHAR(50)
        )"""
        cursor.execute(sql_command)
        db.commit()
        cursor.close()

class AddUser:
    def __init__(self, username, user_password):
        self.username = username
        self.user_password = user_password

    def add_user(self):
        db = DataBase().connect_to_database()
        cursor = db.cursor(buffered=True)
        _UserTable().create_table()
        sql_command = "INSERT INTO users (username, password) VALUES (%s, %s)"
        content = (self.username, self.user_password)
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

    
# TODO: remove before production
def allUsers():
    db = DataBase().connect_to_database()
    cursor = db.cursor(buffered=True)
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    print(users)
    cursor.close()
    return users

# test
def all_user_names():
    db = DataBase().connect_to_database()
    cursor = db.cursor(buffered=True)
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    print(users)
    cursor.close()
    return [name[1] for name in users]

