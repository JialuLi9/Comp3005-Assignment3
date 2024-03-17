# Comp3005-Assignment3
Student Name: Jialu Li
Student ID: 101260696

INSTALL INSTRUCTIONS:
1. Install python if needed.
2. Install PostgreSQL if needed.
3. Install psycopg2 using 'pip install psycopg2-binary'

To launch the program, run the command below in the terminal: 
python3 main.py

TESTING INSTRUCTIONS:
1. Copy the text in createTable.txt to PostgreSQL Query tool create the table names "students"

2. Copy the text in intialData.txt to PostgreSQL Query tool to intialize the data

3. Test the various functions :
(Please ensure that only one function is retained within the main method, as any query executed will modify the data. Subsequent executions of the same query may not work due to these changes.)

a) getAllStudents(): retrieves and displays all records from the students table
b) addStudent(first_name, last_name, email, enrollment_date): inserts a new student record into the students table with the infomation be passed in
c) updateStudentEmail(student_id, new_email): updates the email address by specified student_id
d) deleteStudent(student_id): deletes the record of the student by specified student_id


This is the link to the demonstration:
https://youtu.be/z0cHIt9xBRA
