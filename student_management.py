"""
This script models student behavior at Global Tech University using object-oriented programming in Python.

Main Features:
- `Student` class: Models regular students with name, ID, major, and course enrollment.
- `GraduateStudent` class: Inherits from Student, adds thesis topic, advisor, and program fee.
- Detailed docstrings for clarity and documentation.
- Demonstrates method overriding, inheritance, and use of super().
- Implements error handling in course operations.
"""


class Student:
    """
    A class to represent a student at Global Tech University.

    Attributes:
        school_name (str): Shared by all students.
        name (str): Student's name.
        student_id (int): Unique student ID.
        major (str): Student's major field.
        courses (list): Courses the student is enrolled in.
    """

    school_name = "Global Tech University"

    def __init__(self, name, student_id, major) -> None:
        """
        Initialize the student with name, student ID, major, and an empty list of courses.
        """
        self.name = name
        self.student_id = student_id
        self.major = major
        self.courses = []

    def enroll_course(self, course_name):
        """
        Enroll the student in a course.

        Args:
            course_name (str): The course to enroll in.
        """
        self.courses.append(course_name)
        print(f"[Enroll] {self.name} has enrolled in '{course_name}'.")

    def drop_course(self, course_name):
        """
        Drop a course the student is enrolled in.

        Args:
            course_name (str): The course to drop.

        Handles:
            ValueError: If course is not in enrolled list.
        """
        if course_name not in self.courses:
            print(
                f"[Drop Error] '{course_name}' not found in {self.name}'s enrolled courses."
            )
            return
        try:
            self.courses.remove(course_name)
            print(f"[Drop] {self.name} has successfully dropped '{course_name}'.")
        except ValueError:
            print(f"[Exception] Unexpected error while removing '{course_name}'.")

    def get_student_info(self):
        """
        Print student details including name, ID, major, school, and courses.
        """
        print(f"\n--- Student Information ---")
        print(f"Name       : {self.name}")
        print(f"Student ID : {self.student_id}")
        print(f"Major      : {self.major}")
        print(f"School     : {self.school_name}")
        print(f"Enrolled Courses: {self.courses}")

    def display_enrolled_courses(self):
        """
        Display the list of enrolled courses.
        """
        print(f"\n--- Enrolled Courses for {self.name} ---")
        if self.courses:
            for course in self.courses:
                print(f"- {course}")
        else:
            print("[Notice] No courses currently enrolled.")


class GraduateStudent(Student):
    """
    A subclass of Student representing a graduate-level student.

    Additional Attributes:
        thesis_topic (str): The thesis topic of the graduate student.
        advisor (str): Assigned advisor for thesis guidance.
        graduate_program_fee (int): Constant fee for graduate program.
    """

    graduate_program_fee = 5000  # Class attribute

    def __init__(self, name, student_id, major, thesis_topic) -> None:
        """
        Initialize a graduate student with all inherited attributes and thesis topic.
        """
        super().__init__(name, student_id, major)
        self.thesis_topic = thesis_topic
        self.advisor = None  # Will be set later

    def set_advisor(self, advisor_name):
        """
        Assign an advisor to the graduate student.

        Args:
            advisor_name (str): The advisor's name.
        """
        self.advisor = advisor_name
        print(f"[Advisor Assigned] {self.name}'s advisor set to '{self.advisor}'.")

    def get_student_info(self):
        """
        Print complete student information, including thesis and advisor.

        Overrides:
            Student.get_student_info
        """
        super().get_student_info()  # Call parent method
        print(f"\n--- Graduate Program Info ---")
        print(f"Thesis Topic     : {self.thesis_topic}")
        print(f"Advisor          : {self.advisor if self.advisor else 'Not Assigned'}")
        print(f"Program Fee      : {self.graduate_program_fee}")


# ---------------------- Regular Student Tests ----------------------

student1 = Student("Alice", 101, "Computer Science")
student1.enroll_course("Math 101")
student1.enroll_course("Physics 201")
student1.enroll_course("English Lit")
student1.drop_course("Physics 201")
student1.drop_course("History 101")  # This will trigger an error
student1.display_enrolled_courses()
student1.get_student_info()

student2 = Student("Bob", 102, "Mechanical Engineering")
student2.enroll_course("Thermodynamics")
student2.enroll_course("Material Science")
student2.get_student_info()
student2.display_enrolled_courses()

# ---------------------- Graduate Student Tests ----------------------

print("\n====== Graduate Student Demonstration ======\n")

grad_student = GraduateStudent("Charlie", 201, "Data Science", "AI for Healthcare")
grad_student.enroll_course("Machine Learning")
grad_student.enroll_course("Deep Learning")
grad_student.set_advisor("Dr. Smith")
grad_student.get_student_info()
grad_student.display_enrolled_courses()
