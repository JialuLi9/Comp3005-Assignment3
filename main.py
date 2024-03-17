import psycopg2
# SELECT * FROM students

# Function for connecting the database
def get_db_connection():
    connection = psycopg2.connect(
        dbname='assignments',
        user='postgres',
        password='Jialu0918/',
        host='localhost'
    )
    return connection

# Function for getting all the students
def get_all_students():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM students')
    records = cursor.fetchall()
    for record in records:
        print(record)
    cursor.close()
    connection.close()

# CRUD operations - get all students
def add_student(first_name, last_name, email, enrollment_date):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute(
        'INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s)',
        (first_name, last_name, email, enrollment_date)
    )
    connection.commit()
    print(f"Student {first_name} {last_name} added.")
    cursor.close()
    connection.close()

# Update student email
def update_student_email(student_id, new_email):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute(
        'UPDATE students SET email = %s WHERE student_id = %s',
        (new_email, student_id)
    )
    connection.commit()
    print(f"Student ID {student_id}'s email updated to {new_email}.")
    cursor.close()
    connection.close()

# Delete student by id
def delete_student(student_id):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute(
        'DELETE FROM students WHERE student_id = %s',
        (student_id,)
    )
    connection.commit()
    print(f"Student ID {student_id} deleted.")
    cursor.close()
    connection.close()

if __name__ == "__main__":
    
    get_all_students();
    
    #add_student("Annie", "Chika", "756498@gamil.com", "2023-09-05");
    

    #update_student_email(4, "helloworld@gmail.com");
    

    #delete_student(1);
    
