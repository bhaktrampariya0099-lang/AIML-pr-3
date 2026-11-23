students=[]
print("Welcome to the Student Data Organizer!")

while True:
    
    print("Select an option:")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Update Student Information")
    print("4. Delete Student")
    print("5. Display Subjects Offered")
    print("6. Exit")

    choice = input("Enter your choice: ")

    
    if choice == "1":
        print("Enter student details:")

        student_id = input("Student ID: ")

        found = False
        for student in students:
            if student["ID"] == student_id:
                found = True

        if found:
            print("Student ID already exists!")
        else:
            name = input("Name: ")
            age = int(input("Age: "))
            grade = input("Grade: ")
            dob = input("Date of Birth (YYYY-MM-DD): ")
            subjects = input("Subjects (comma-separated): ").split(",")

            student = {
                "ID": student_id,
                "Name": name,
                "Age": age,
                "Grade": grade,
                "DOB": dob,
                "Subjects": [s.strip() for s in subjects]
            }

            students.append(student)
            print("Student added successfully!")

    
    elif choice == "2":
        print("--- Display All Students ---")

        if len(students) == 0:
            print("No students found!")
        else:
            for student in students:
                print("Student ID:", student["ID"])
                print("Name:", student["Name"])
                print("Age:", student["Age"])
                print("Grade:", student["Grade"])
                print("DOB:", student["DOB"])
                print("Subjects:", ", ".join(student["Subjects"]))

    
    elif choice == "3":
        student_id = input("Enter Student ID to update: ")

        found = False

        for student in students:
            if student["ID"] == student_id:
                found = True

                print("\nEnter new information:")
                student["Name"] = input("Name: ")
                student["Age"] = int(input("Age: "))
                student["Grade"] = input("Grade: ")
                student["DOB"] = input("Date of Birth: ")
                subjects = input("Subjects: ")
                student["Subjects"] = [
                    s.strip() for s in subjects.split(",")
                ]

                print("\nStudent updated successfully!")
                break

        if not found:
            print("Student not found!")

    
    elif choice == "4":
        student_id = input("Enter Student ID to delete: ")

        found = False

        for student in students:
            if student["ID"] == student_id:
                students.remove(student)
                found = True
                print("\nStudent deleted successfully!")
                break

        if not found:
            print("Student not found!")

    
    elif choice == "5":
        print("--- Display Subjects Offered ---")

        all_subjects = []

        for student in students:
            for subject in student["Subjects"]:
                if subject not in all_subjects:
                    all_subjects.append(subject)

        if len(all_subjects) == 0:
            print("No subjects available!")
        else:
            for subject in all_subjects:
                print("-", subject)

    
    elif choice == "6":
        print("Thank you for using Student Data Organizer!")
        break

    else:
        print("Invalid choice! Please try again.")