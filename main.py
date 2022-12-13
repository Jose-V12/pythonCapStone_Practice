import mysql.connector
from mysql.connector import Error
def create_server_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection
def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Database created successfully")
    except Error as err:
        print(f"Error: '{err}'")
def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query successful")
    except Error as err:
        print(f"Error: '{err}'")
def read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as err:
        print(f"Error: '{err}'")

create_teacher_table = """ 
CREATE TABLE teacher (
  teacher_id INT PRIMARY KEY,
  first_name VARCHAR(40) NOT NULL,
  last_name VARCHAR(40) NOT NULL,
  language_1 VARCHAR(3) NOT NULL,
  dob DATE,
  tax_id INT UNIQUE,
  phone_no VARCHAR(20)
  );
 """
table_teacher = """
INSERT INTO teacher VALUES
(1,  'James', 'Smith', 'ENG','1985-04-20', 12345, '+491774553676'),
(2, 'Stefanie',  'Martin',  'FRA',   '1970-02-17', 23456, '+491234567890'), 
(3, 'Steve', 'Wang',  'MAN',  '1990-11-12', 34567, '+447840921333'),
(4, 'Friederike',  'Müller-Rossi', 'DEU',  '1987-07-07',  45678, '+492345678901'),
(5, 'Isobel', 'Ivanova', 'RUS',  '1963-05-30',  56789, '+491772635467'),
(6, 'Niamh', 'Murphy', 'ENG',  '1995-09-08',  67890, '+491231231232');
"""
display = """
SELECT *
FROM teacher;
"""
#updating information in teacher table
update = """
UPDATE teacher
SET last_name="Greene" 
WHERE first_name = "Stefanie";
"""
delete_employee = """
DELETE FROM teacher 
WHERE first_name = "Stefanie"
"""
drop_table = """
DROP TABLE teacher
"""
drop_db = """
DROP DATABASE hospital"""
connection = create_server_connection("localhost", "root", "student", "hospital")
execute_query(connection, drop_db)
#results = read_query(connection, display)
#for result in results:
 #   print(result)