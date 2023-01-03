from database import DataBase

class _CreateGuardsTable:
    def create_table(self):
        db = DataBase().connect_to_database()
        cursor = db.cursor(buffered=True)
        sql_command = """CREATE TABLE IF NOT EXISTS guards(
        Pers_No VARCHAR(50) primary key,
        Surname VARCHAR(50),
        First_Name VARCHAR(50),
        ID_No VARCHAR(50),
        Contact_Tel_No VARCHAR(50),
        Address VARCHAR(100),
        Date_Started VARCHAR(50),
        Default_Site_id VARCHAR(50)
        )"""
        cursor.execute(sql_command)
        db.commit()
        cursor.close()

class AddGuard:
    def __init__(self, 
        Pers_No, Surname, First_Name, ID_No, Contact_Tel_No, Address, Date_Started, Default_Site_id):
        self.Pers_No = Pers_No
        self.Surname = Surname
        self.First_Name = First_Name
        self.ID_No = ID_No
        self.Contact_Tel_No = Contact_Tel_No
        self.Address = Address
        self.Date_Started = Date_Started
        self.Default_Site_id = Default_Site_id
        

    def add_guard(self):
        db = DataBase().connect_to_database()
        cursor = db.cursor(buffered=True)
        _CreateGuardsTable().create_table()
        sql_command = """INSERT INTO guards 
            (Pers_No, Surname, 
            First_Name, 
            ID_No,Contact_Tel_No,
            Address, 
            Date_Started, 
            Default_Site_id)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
        content = (
            self.Pers_No, 
            self.Surname, 
            self.First_Name, 
            self.ID_No, 
            self.Contact_Tel_No, 
            self.Address, 
            self.Date_Started, 
            self.Default_Site_id,
        )
        cursor.execute(sql_command, content)
        db.commit()
        cursor.close()

def all_guard_pers():
    db = DataBase().connect_to_database()
    cursor = db.cursor(buffered=True)
    cursor.execute("SELECT * FROM guards")
    guards = cursor.fetchall()
    cursor.close()
    return [pers_no[0] for pers_no in guards]