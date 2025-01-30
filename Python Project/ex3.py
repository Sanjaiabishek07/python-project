students = [
    {"id": 1, "name": "Rajesh"},
    {"id": 2, "name": "Rahul"},
    {"id": 3, "name": "Sruthi"},
    {"id": 4, "name": "Sujith"}
]

def find_student_name(student_id):
    for student in students:
        if student["id"] == student_id:
            return student["name"]
    return "Student not found"


student_id = int(input("Enter the student ID: "))
student_name = find_student_name(student_id)
print(f"Student name: {student_name}")