from database import DataBase

class _CreateTable:
    def create_table(self):
        db = DataBase().connect_to_database()
        cursor = db.cursor(buffered = True)
        sql_command = '''CREATE TABLE IF NOT EXISTS penalties(
                        id INTEGER NOT NULL AUTO_INCREMENT primary key,
                        location VARCHAR(50),
                        officer VARCHAR(50),
                        penalty VARCHAR(500),
                        site VARCHAR(50),
                        report VARCHAR(2000),
                        supervisor VARCHAR(50),
                        date VARCHAR(50),
                        time VARCHAR(50),
                        signature MEDIUMBLOB
                        )'''
        cursor.execute(sql_command)
        db.commit()

class AddPenaltyGiven:
    def __init__(
        self, location, officer, penalty, site, 
        report, supervisor, date, time):

        self.location = location
        self.officer = officer
        self.penalty = penalty
        self.site = site
        self.report = report
        self.supervisor = supervisor
        self.date = date
        self.time = time

    def add_penalty_given(self):
        _CreateTable().create_table()

        try:
            with open("signatures.png", "rb") as image:
                binary_data = image.read()
        except:
            binary_data = None

        db = DataBase().connect_to_database()
        cursor = db.cursor(buffered = True)

        sql_command = '''INSERT INTO penalties(
            location, officer, penalty, site, 
            report, supervisor, date, time, signature) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)'''

        content = (
            self.location, self.officer, self.penalty, self.site,
            self.report, self.supervisor, self.date, self.time, binary_data
        )
        cursor.execute(sql_command, content)
        db.commit()
        cursor.close()


        