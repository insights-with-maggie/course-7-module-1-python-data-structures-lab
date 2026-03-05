from lib.student_data import get_students
from lib.filter import filter_students_by_major
from lib.data_processing import display_students, format_student_data
from lib.set_operations import unique_majors, add_course_for_student, student_courses_union
from lib.data_generator import students_by_major_generator


def main():
    """Run a demonstration of the student data system."""
    # Load all student records
    students = get_students()

    print("=== All Students ===")
    display_students(students)
    print()

    print("=== Filter: Computer Science Students ===")
    cs_students = filter_students_by_major(students, "Computer Science")
    display_students(cs_students)
    print()

    print("=== Unique Majors (Set Comprehension) ===")
    majors = unique_majors(students)
    print(majors)

    print()

    print("=== Generator: Physics Students (Lazy Evaluation) ===")
    physics_gen = students_by_major_generator(students, "Physics")
    for s in physics_gen:
        print(format_student_data(s))
    print()

    print("=== Example: Track Completed Courses with Sets ===")
    course_map = {}
    add_course_for_student(course_map, 101, "CS101")
    add_course_for_student(course_map, 101, "MTH100")
    add_course_for_student(course_map, 102, "MTH100")
    add_course_for_student(course_map, 103, "PHY101")

    print("Courses map:", course_map)
    print("Union of courses for [101, 102]:", student_courses_union(course_map, [101, 102]))


# Standard Python entry point
if __name__ == "__main__":
    main()
