# This module contains functions for filtering student data.

def filter_students_by_major(students, major):
    result = []

    for student in students:
        if student[2] == major:
            result.append(student)

    return result
