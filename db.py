import mysql.connector as connector

#db credentials
HOST = "localhost"
USER = "root"
PASSWORD = ""
DATABASE = "universities"

#connect database.. 
db = connector.connect(
    host=HOST,
    user=USER,
    password=PASSWORD,
    database=DATABASE
)

dbCursor = db.cursor()

# Create table if doesn't exist
def create_table():
    sql = """CREATE TABLE IF NOT EXISTS `data` (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255) , country VARCHAR(90), website VARCHAR(100))"""
    dbCursor.execute(sql)
    db.commit()

#save data for later use
def save_university_data(universityData):
    sql = "INSERT IGNORE INTO data (name, country, website) VALUES (%s, %s, %s)"

    for university in universityData:
        count = 0
        values = university
        dbCursor.execute(sql,values)
        db.commit()
        count +=1
    print("Inserted : " + str(count) + " rows.")