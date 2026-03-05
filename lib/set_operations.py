# This module contains operations related to sets.

def get_unique_majors(students):
    majors = set()

    for student in students:
        majors.add(student[2])

    return majors
