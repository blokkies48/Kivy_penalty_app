from Confidential.Database.Database import DB, CURSOR

class _UserTable:
    def create_table(self):
        sql_command = """CREATE TABLE IF NOT EXISTS users(
        id INTEGER AUTO_INCREMENT primary key,
        username VARCHAR(50) ,
        password VARCHAR(50)
        )"""
        CURSOR.execute(sql_command)
        DB.commit()

class AddUser:
    def __init__(self, username, user_password):
        self.username = username
        self.user_password = user_password

    def add_user(self):
        _UserTable().create_table()
        sql_command = "INSERT INTO users (username, password) VALUES (%s, %s)"
        content = (self.username, self.user_password)
        CURSOR.execute(sql_command, content)
        DB.commit()

class CurrentUser:
    def get_user(self, username):
        CURSOR.execute(f"SELECT * FROM users WHERE username = '{username}'" )
        return CURSOR.fetchone()

    
# TODO: remove before production
def allUsers():
    CURSOR.execute("SELECT * FROM users")
    users = CURSOR.fetchall()
    print(users)
    return users

# test
def all_user_names():
    CURSOR.execute("SELECT * FROM users")
    users = CURSOR.fetchall()
    print(users)
    return [name[1] for name in users]

