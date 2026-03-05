from lib.data_generator import student_generator
from lib.student_data import get_students


def test_student_generator():
    students = get_students()

    math_students = student_generator(students, "Mathematics")

    assert next(math_students)[1] == "Bob Smith"
    assert next(math_students)[1] == "Eve Lewis"
