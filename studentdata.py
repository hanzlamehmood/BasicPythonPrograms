def add_student(s):
    roll_number = input("Enter the roll number: ")
    name = input("Enter the student's name: ")
    father_name = input("Enter the father's name: ")
    student_class = input("Enter the class: ")
    field_of_study = input("Enter the field of study: ")

    s[roll_number] = {"Name": name, "Father's Name": father_name, "Class": student_class,
        "Field of Study": field_of_study}


def display_student(s):
    roll_number = input("Enter the roll number to display: ")
    if roll_number in s:
        student = s[roll_number]
        print("\nStudent Information:")
        print(f"Roll Number: {roll_number}")
        print(f"Name: {student['Name'].title()}")
        print(f"Father's Name: {student["Father's Name"].title()}")
        print(f"Class: {student['Class']}")
        print(f"Field of Study: {student['Field of Study'].title()}")
    else:
        print("No student found with that roll number.")


students = {}
while True:
    print("\nOptions:")
    print("1. Add Student")
    print("2. Display Student")
    print("3. Exit")
    choice = input("Enter your choice (1/2/3): ")
    if choice == '1':
        add_student(students)
    elif choice == '2':
        display_student(students)
    elif choice == '3':
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")