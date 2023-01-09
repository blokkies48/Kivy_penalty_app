from database import DataBase

class _CreateTable:
    def create_table(self):
        db = DataBase().connect_to_database()
        cursor = db.cursor(buffered = True)
        sql_command = '''CREATE TABLE IF NOT EXISTS penalties_list(
                        offenses VARCHAR(50) primary key,
                        penalties VARCHAR(50),
                        description VARCHAR(500)
                        )'''
        cursor.execute(sql_command)
        db.commit()

class AddPenalty:
    def __init__(self, offenses, penalties, description):
        self.offenses = offenses
        self.penalties = penalties
        self.description = description

    def add_penalty(self):
        db = DataBase().connect_to_database()
        cursor = db.cursor(buffered = True)
        _CreateTable().create_table()
        sql_command = '''INSERT INTO penalties_list(
            offenses, penalties, description) VALUES (%s, %s, %s)'''
        content = (
            self.offenses, self.penalties, self.description
        )
        cursor.execute(sql_command, content)
        db.commit()
        cursor.close()

def get_penalties():
    db = DataBase().connect_to_database()
    cursor = db.cursor(buffered=True)
    cursor.execute("SELECT * FROM penalties_list")
    penalties_list = cursor.fetchall()
    cursor.close()
    return [(penalties[0], penalties[1]) for penalties in penalties_list]