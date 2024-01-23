import sqlite3

# connect database using SQlite3 as database
conn = sqlite3.connect('database.db')
print("opened database successfully")

# create table students
conn.execute('''CREATE TABLE IF NOT EXISTS students (
             id INTEGER PRIMARY KEY, 
             email TEXT NOT NULL, 
             fullname TEXT NOT NULL
)''')
print("students table created successfully")

# create table store
conn.execute('''CREATE TABLE IF NOT EXISTS store(
             id INTEGER PRIMARY KEY AUTOINCREMENT,
             name TEXT,
             address TEXT
)''')
print("store table created successfully")

# create table 'tables'
conn.execute('''CREATE TABLE IF NOT EXISTS tables(
             id INTEGER PRIMARY KEY AUTOINCREMENT,
             number INTEGER,
             guestno INTEGER,
             FOREIGN KEY (store_id) REFERENCES store (id)
)''')
print("tables table created successfully")


# create table booking
conn.execute('''CREATE TABLE IF NOT EXISTS booking(
             id INTEGER PRIMARY KEY AUTOINCREMENT,
             bookingdate TEXT,
             booking_starttime TEXT,
             booking_endtime TEXT, 
             booking_status TEXT,
             FOREIGN KEY (students_id) REFERENCES students (id)
             FOREIGN KEY (tables_id) REFERENCES tables (id)
)''')

conn.commit()
conn.close()