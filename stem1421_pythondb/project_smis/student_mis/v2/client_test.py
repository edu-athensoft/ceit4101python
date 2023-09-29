"""
Test of Client
"""

import mydbutil

from studentdao import *


# settings
DB_NAME = 'smis'

# Example usage:
if __name__ == "__main__":
    conn = mydbutil.get_connection(DB_NAME)
    student_dao = StudentDao(conn)

    # Create a new student
    STUDENT_ID = 9001
    new_student = Student(STUDENT_ID, "Alice", "XYZ School", "5")
    student_dao.create_student(new_student)

    # Retrieve and update a student
    retrieved_student = student_dao.get_student(STUDENT_ID)
    if retrieved_student:
        print("Retrieved Student:", retrieved_student)
        retrieved_student.studentName = "Alicia"
        student_dao.update_student(retrieved_student)

    # Delete a student
    student_dao.delete_student(STUDENT_ID)

    # close connection
    conn.close()
