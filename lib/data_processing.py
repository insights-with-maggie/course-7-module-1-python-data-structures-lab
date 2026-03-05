# This module contains functions to process student data.

def format_student_data(student):
    student_id, name, major = student
    return f"ID: {student_id} | Name: {name} | Major: {major}"


def display_students(students):
    for student in students:
        print(format_student_data(student))