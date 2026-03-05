# This module contains functions to lazily generate student data.

def student_generator(students, major):
    for student in students:
        if student[2] == major:
            yield student
