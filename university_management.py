"""
This script models university members using object-oriented programming.

Main Features:
- Base class `UniversityPerson` with encapsulated name and email attributes.
- Subclasses `Faculty` and `Student` inherit from `UniversityPerson`.
- Demonstrates polymorphism via method overriding (`display_basic_info()`).
- Includes property decorators for name and email with validation.
- Encapsulation using protected attributes.
- A shared interface method is called on different subclass objects.
"""

import re


class UniversityPerson:
    """
    A base class representing a person in the university system.

    Attributes:
        _name (str): Protected name of the person.
        _email (str): Protected email address (validated via setter).
    """

    def __init__(self, name) -> None:
        """
        Initialize with name and default email as None.
        """
        self._name = name
        self._email = None

    @property
    def name(self):
        """
        Get the name of the person.
        """
        return self._name

    @name.setter
    def name(self, new_value):
        """
        Set the name of the person.
        """
        self._name = new_value
        print(f"[Update] Name updated to '{new_value}'.")

    @property
    def email(self):
        """
        Get the email of the person. Returns "N/A" if email is not set.
        """
        return self._email if self._email else "N/A"

    @email.setter
    def email(self, new_email):
        """
        Set and validate the email of the person.
        """
        if re.match(r"[^@]+@[^@]+\.[^@]+", new_email):
            self._email = new_email
            print(f"[Update] Email set to '{new_email}'.")
        else:
            print(f"[Error] Invalid email format: '{new_email}'.")

    def display_basic_info(self):
        """
        Display the person's basic information (name and email).
        """
        print(f"Name: {self._name}, Email: {self._email}")


class Faculty(UniversityPerson):
    """
    Represents a faculty member.

    Attributes:
        _department (str): Department the faculty belongs to.
        _rank (str): Rank (e.g., Assistant, Associate, Full Professor).
    """

    def __init__(self, name, department, rank) -> None:
        """
        Initialize with name, department, and rank.
        """
        super().__init__(name)
        self._department = department
        self._rank = rank

    def display_basic_info(self):
        """
        Override: Display basic info and department/rank.
        """
        super().display_basic_info()
        print(f"Department: {self._department}, Rank: {self._rank}")

    def teach_course(self, course_name):
        """
        Simulate teaching a course.
        """
        print(f"{self._name} is teaching '{course_name}'.")


class Student(UniversityPerson):
    """
    Represents a student at the university.

    Attributes:
        _student_id (int): Unique identifier for the student.
    """

    def __init__(self, name, student_id) -> None:
        """
        Initialize with name and student ID.
        """
        super().__init__(name)
        self._student_id = student_id

    def display_basic_info(self):
        """
        Override: Display basic info and student ID.
        """
        super().display_basic_info()
        print(f"Student ID: {self._student_id}")

    def enroll_in_class(self, course_name):
        """
        Simulate enrolling in a course.
        """
        print(f"{self._name} enrolled in '{course_name}'.")


print("\n====== University Members Demo (Polymorphism) ======\n")

university_members = []

faculty_member = Faculty("Dr. John Smith", "Computer Science", "Associate Professor")
faculty_member.email = "john.smith@gtu.edu"
university_members.append(faculty_member)

student_member = Student("Emily Johnson", 202301)
student_member.email = "invalid-email"
student_member.email = "emily.j@gtu.edu"
university_members.append(student_member)

print("\n--- Displaying Info for All University Members ---\n")
for member in university_members:
    member.display_basic_info()
    print("-" * 50)
