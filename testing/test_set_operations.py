from lib.set_operations import get_unique_majors
from lib.student_data import get_students


def test_get_unique_majors():
    students = get_students()

    majors = get_unique_majors(students)

    assert "Computer Science" in majors
    assert "Mathematics" in majors
