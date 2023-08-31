if connection.is_connected():
    cursor=connection.cursor()
    create_table_query="create table student(Student_ID int AUTO_INCREMENT primary key,Name varchar(40),age int)"
    cursor.execute(create_table_query)
