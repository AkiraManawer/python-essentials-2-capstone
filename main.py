from models import Student
from data_tools import (
    generate_data_file,
    load_students,
    export_report,
    log_event,
)
from analytics import (
    passing_students,
    make_grader,
    class_average,
    highest,
    lowest,
    pass_rate,
    first_three_scores,
)
from reporting import environment_report, date_report


def create_student_objects(records):
    students = []
    for index, (name, score) in enumerate(records, start=1):
        student_id = f"S{index}"
        student = Student(name, student_id, score)
        students.append(student)
    return students


def show_menu():
    print("\n--- Student ANALYTICS TOOLKIT ---")
    print("1. Generate sample data file")
    print("2. Load and clean records from file")
    print("3. View all students")
    print("4. Analyse (averages, pass/fail, top student)")
    print("5. Filter students (generator)")
    print("6. Grade with a custom pass mark (closure)")
    print("7. Environment and date report")
    print("8. Export results to a file")
    print("9. Exit")


students = []
last_report = ""

while True:
    show_menu()
    choice = input("Enter your choice (1-9): ")
    try:
        choice = int(choice)
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 9.")
        continue
    if choice == 1:
        message = generate_data_file()
        print(message)
        log_event("Generated sample data")
    elif choice == 2:
        try:
            records = load_students()
            students = create_student_objects(records)
            print(f"Loaded {len(students)} students loaded successfully.")
            log_event("Loaded and cleaned student records")
        except FileNotFoundError:
            print("Data file not found. Please generate the data file first.")
    elif choice == 3:
        if not students:
            print("No student records available. Choose option 2 first.")
        else:
            print("\n--- ALL STUDENTS ---")
            for student in students:
                print(student)
    elif choice == 4:
        if not students:
            print("No student records available. Choose option 2 first.")
        else:
            average = class_average(students)
            top_student = highest(students)
            lowest_student = lowest(students)
            rate = pass_rate(students)

            passed = sum(student.has_passed() for student in students)
            failed = len(students) - passed

            last_report = f"""
===== CLASS ANALYSIS =====
Class average: {average:.2f}
Passed students: {passed}
Failed students: {failed}
Pass rate: {rate:.2f}%
Highest student: {top_student.name} ({top_student.score})
Lowest student: {lowest_student.name} ({lowest_student.score})
First three scores: {first_three_scores(students)}
"""

            print(last_report)
            log_event("Performed class analysis")

    elif choice == 5:
        if not students:
            print("No students loaded. Choose option 2 first.")
        else:
            print("\n===== PASSING STUDENTS =====")

            for student in passing_students(students):
                print(student)

            log_event("Displayed passing students using generator")

    elif choice == 6:
        if not students:
            print("No students loaded. Choose option 2 first.")
        else:
            pass_mark_input = input("Enter a custom pass mark: ")

            try:
                pass_mark = int(pass_mark_input)

                grader = make_grader(pass_mark)

                print(f"\nStudents passing with a mark of {pass_mark}:")

                for student in students:
                    result = grader(student.score)
                    print(f"{student.name}: {student.score} - {result}")

                normal_grader = make_grader(50)

                print("\nExample of two different graders:")
                print("Score 55 with pass mark 50:", normal_grader(55))
                print("Score 55 with pass mark 60:", make_grader(60)(55))

                log_event("Used custom pass mark closure")

            except ValueError:
                print("Invalid pass mark. Please enter a whole number.")

    elif choice == 7:
        print(environment_report())
        print(date_report())
        log_event("Displayed environment and date reports")

    elif choice == 8:
        if not last_report:
            print("No analysis report available. Choose option 4 first.")
        else:
            message = export_report(last_report)
            print(message)
            log_event("Exported analysis report")

    elif choice == 9:
        print("Thank you for using Student Analytics Toolkit.")
        log_event("Exited program")
        break

    else:
        print("Invalid choice. Please select a number from 1 to 9.")
