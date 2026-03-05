from lib.filter import filter_students_by_major
from lib.student_data import get_students


def test_filter_students_by_major():
    students = get_students()

    cs_students = filter_students_by_major(students, "Computer Science")

    assert len(cs_students) == 3


def test_filter_no_results():
    students = get_students()

    result = filter_students_by_major(students, "Astronomy")

    assert result == []
