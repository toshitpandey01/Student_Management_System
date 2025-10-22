from db_config import get_connection

def add_student(roll_no, name, age, course, marks):
    conn = get_connection()
    cursor = conn.cursor()
    query = "INSERT INTO students (roll_no, name, age, course, marks) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(query, (roll_no, name, age, course, marks))
    conn.commit()
    conn.close()
    print("✅ Student added successfully!")

def view_students():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    result = cursor.fetchall()
    conn.close()
    for row in result:
        print(row)

def update_marks(roll_no, marks):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE students SET marks=%s WHERE roll_no=%s", (marks, roll_no))
    conn.commit()
    conn.close()
    print("✅ Marks updated successfully!")

def delete_student(roll_no):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE roll_no=%s", (roll_no,))
    conn.commit()
    conn.close()
    print("✅ Student deleted successfully!")

def search_student(roll_no):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students WHERE roll_no=%s", (roll_no,))
    result = cursor.fetchone()
    conn.close()
    if result:
        print(result)
    else:
        print("❌ Student not found.")