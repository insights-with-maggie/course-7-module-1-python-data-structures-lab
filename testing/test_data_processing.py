from lib.data_processing import format_student_data, display_students
from lib.student_data import get_students


def test_format_student_data():
    student = (101, "Alice Johnson", "Computer Science")
    expected = "ID: 101 | Name: Alice Johnson | Major: Computer Science"

    assert format_student_data(student) == expected


def test_display_students(capsys):
    students = get_students()

    display_students(students)

    captured = capsys.readouterr()

    assert "Alice Johnson" in captured.out
