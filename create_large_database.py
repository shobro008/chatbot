import sqlite3

# Connect to SQLite database (it will create the file if it doesn't exist)
conn = sqlite3.connect('company_large.db')
conn.execute("PRAGMA foreign_keys = 1")  # Enable foreign key support

# Create a cursor object
cursor = conn.cursor()

# Drop existing tables if they exist
cursor.execute("DROP TABLE IF EXISTS Employees")
cursor.execute("DROP TABLE IF EXISTS Departments")

# Create the Departments table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Departments (
    ID INTEGER PRIMARY KEY,
    Name TEXT NOT NULL UNIQUE,
    Manager TEXT NOT NULL
);
''')

# Create the Employees table with AUTOINCREMENT for the ID column and foreign key constraint
cursor.execute('''
CREATE TABLE IF NOT EXISTS Employees (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT NOT NULL,
    Department TEXT NOT NULL,
    Position TEXT NOT NULL,
    Salary REAL NOT NULL,
    Hire_Date TEXT NOT NULL,
    FOREIGN KEY (Department) REFERENCES Departments(Name)
);
''')

# Insert data into Departments table
cursor.executemany('''
INSERT INTO Departments (ID, Name, Manager)
VALUES (?, ?, ?);
''', [
    (1, 'Sales', 'Alice'),
    (2, 'Engineering', 'Bob'),
    (3, 'Marketing', 'Charlie'),
    (4, 'HR', 'Grace')
])

# Insert a larger set of data into Employees table
cursor.executemany('''
INSERT INTO Employees (Name, Department, Position, Salary, Hire_Date)
VALUES (?, ?, ?, ?, ?);
''', [
    ('Alice', 'Sales', 'Manager', 50000, '2021-01-15'),
    ('Bob', 'Engineering', 'Manager', 70000, '2020-06-10'),
    ('Charlie', 'Marketing', 'Manager', 60000, '2022-03-20'),
    ('David', 'Sales', 'Sales Representative', 55000, '2019-11-22'),
    ('Eva', 'Engineering', 'Senior Engineer', 75000, '2018-07-05'),
    ('Frank', 'Marketing', 'Marketing Specialist', 65000, '2020-12-10'),
    ('Grace', 'HR', 'Manager', 48000, '2021-09-01'),
    ('Helen', 'Engineering', 'Software Engineer', 72000, '2019-03-15'),
    ('Ivy', 'Sales', 'Sales Representative', 52000, '2022-05-18'),
    ('Jack', 'Marketing', 'Content Creator', 63000, '2019-02-02'),
    ('Karl', 'HR', 'HR Specialist', 50000, '2020-10-13'),
    ('Lily', 'Engineering', 'Software Engineer', 71000, '2021-06-30'),
    ('Mike', 'Sales', 'Sales Representative', 56000, '2022-08-14'),
    ('Nancy', 'HR', 'Recruiter', 49000, '2021-04-23'),
    ('Oscar', 'Engineering', 'Senior Engineer', 73000, '2020-01-05'),
    ('Peter', 'Marketing', 'Digital Marketer', 64000, '2021-07-22'),
    ('Quincy', 'HR', 'HR Specialist', 51000, '2022-02-28'),
    ('Rita', 'Engineering', 'Software Engineer', 71000, '2018-11-11'),
    ('Sam', 'Marketing', 'Marketing Analyst', 62000, '2021-03-16'),
    ('Tom', 'Sales', 'Sales Representative', 58000, '2021-12-04'),
    ('Ursula', 'HR', 'HR Specialist', 52000, '2019-04-19'),
    ('Victor', 'Engineering', 'Software Engineer', 74000, '2021-01-10'),
    ('Wendy', 'Marketing', 'Marketing Specialist', 66000, '2022-09-05'),
    ('Xander', 'Sales', 'Sales Representative', 59000, '2020-05-21'),
    ('Yara', 'Engineering', 'Senior Engineer', 78000, '2018-10-08'),
    ('Zoe', 'HR', 'Recruiter', 53000, '2019-07-29'),
    ('Aaron', 'Sales', 'Sales Representative', 54000, '2021-08-01'),
    ('Brenda', 'Engineering', 'Software Engineer', 71000, '2019-12-15'),
    ('Clara', 'Marketing', 'Content Creator', 67000, '2022-04-12'),
    ('Dennis', 'Sales', 'Sales Representative', 53000, '2021-11-23'),
    ('Ella', 'Engineering', 'Software Engineer', 73000, '2020-08-17'),
    ('Felix', 'Marketing', 'Digital Marketer', 68000, '2022-01-10'),
    ('George', 'HR', 'HR Specialist', 51000, '2019-03-10'),
    ('Holly', 'Sales', 'Sales Representative', 56000, '2022-07-25'),
    ('Ian', 'Engineering', 'Senior Engineer', 74000, '2019-09-03'),
    ('Julia', 'Marketing', 'Marketing Analyst', 65000, '2022-06-16'),
    ('Kevin', 'HR', 'HR Specialist', 48000, '2021-11-12'),
    ('Lena', 'Sales', 'Sales Representative', 57000, '2020-12-05'),
    ('Mark', 'Engineering', 'Software Engineer', 75000, '2019-01-22'),
    ('Nina', 'Marketing', 'Marketing Specialist', 66000, '2022-08-21'),
    ('Oscar', 'Sales', 'Sales Representative', 59000, '2021-03-25'),
    ('Paul', 'Engineering', 'Software Engineer', 71000, '2020-07-15'),
    ('Queenie', 'Marketing', 'Content Creator', 67000, '2022-05-29'),
    ('Ray', 'HR', 'Recruiter', 52000, '2019-10-02'),
    ('Sara', 'Sales', 'Sales Representative', 54000, '2020-01-18'),
    ('Tommy', 'Engineering', 'Senior Engineer', 73000, '2018-11-30'),
    ('Uma', 'Marketing', 'Digital Marketer', 69000, '2022-10-17'),
    ('Vera', 'HR', 'HR Specialist', 51000, '2021-06-09'),
    ('William', 'Sales', 'Sales Representative', 60000, '2020-03-04'),
    ('Xenia', 'Engineering', 'Software Engineer', 72000, '2019-05-24'),
    ('Yasmin', 'Marketing', 'Marketing Analyst', 65000, '2022-11-02'),
    ('Zane', 'HR', 'HR Specialist', 53000, '2021-09-12')
])

# Commit changes and close the connection
conn.commit()
conn.close()

print("Large database created and data inserted successfully!")
