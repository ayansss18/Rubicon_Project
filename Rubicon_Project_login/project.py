import mysql.connector

host="localhost"
user="root"
password="@Yansasn9"
database="data_wizard"

connection=mysql.connector.connect(
host=host,
user=user,
password=password,
database=database
)

if connection.is_connected():
    print("connected to database")
else:
    print("Not connected to databse")
    
if connection.is_connected():
    cursor=connection.cursor()
    create_table_query="create table student(Student_ID int AUTO_INCREMENT primary key,Name varchar(40),age int)"
    cursor.execute(create_table_query)
