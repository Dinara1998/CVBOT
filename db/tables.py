from config import db, cursor


def create_tables():
    cursor.execute(''' 
CREATE TABLE IF NOT EXISTS users(
                   user_id INT NOT NULL,
                   first_name TEXT NOT NULL,
                   last_name TEXT,
                   username TEXT,
                   chat_id INT NOT NULL,
                   first_login INT NOT NULL,
                   last_login INT NOT NULL,
                   email TEXT,
                   phone TEXT 

)
 ''' )
    db.commit()

    cursor.execute('''
CREATE TABLE IF NOT EXISTS form(
                   user_id INT,
                   first_name TEXT, 
                   last_name TEXT,
                   phone_number TEXT,
                   email TEXT,
                   city TEXT,
                   location_latitude REAL,
                   location_longitude REAL


)
                         ''')
    db.commit()

    