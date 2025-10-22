from student_manager import *

while True:
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Update Student Marks")
    print("4. Delete Student")
    print("5. Search Student by Roll No")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        roll_no = int(input("Enter Roll No: "))
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        course = input("Enter Course: ")
        marks = float(input("Enter Marks: "))
        add_student(roll_no, name, age, course, marks)

    elif choice == '2':
        view_students()

    elif choice == '3':
        roll_no = int(input("Enter Roll No: "))
        marks = float(input("Enter New Marks: "))
        update_marks(roll_no, marks)

    elif choice == '4':
        roll_no = int(input("Enter Roll No to Delete: "))
        delete_student(roll_no)

    elif choice == '5':
        roll_no = int(input("Enter Roll No to Search: "))
        search_student(roll_no)

    elif choice == '6':
        print("Exiting... Goodbye 👋")
        break

    else:
        print("❌ Invalid choice. Try again.")