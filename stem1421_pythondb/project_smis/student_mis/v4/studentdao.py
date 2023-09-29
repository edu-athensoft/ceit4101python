"""
DAO class of Student
"""

from entity import *
from mydbutil import *


class StudentDao:
    # def __init__(self, connection=None):
    #     self.conn = connection

    def __init__(self, database):
        self.conn = get_connection(database)

    def close(self):
        if self.conn:
            self.conn.close()
            print("[DEBUG] Connection in StudentDao closed")
        else:
            # raise error
            print("[ERROR] Connection in StudentDao can not close due to not existing")

    def create(self, student):
        try:
            connection = self.conn
            with connection.cursor() as cursor:
                # SQL INSERT statement
                sql = "INSERT INTO student (id, student_name, school_name, grade) VALUES (%s, %s, %s, %s)"
                values = (student.studentId, student.studentName, student.schoolName, student.gradeNo)
                cursor.execute(sql, values)
                connection.commit()
                return True
        except pymysql.Error as e:
            print(f"[ERROR] Error creating student: {e}")
            return False
        finally:
            pass

    def get_by_id(self, student_id):
        try:
            connection = self.conn
            with connection.cursor() as cursor:
                # SQL SELECT statement to retrieve a student by studentId
                sql = "SELECT * FROM student WHERE id = %s"
                cursor.execute(sql, student_id)
                result = cursor.fetchone()
                if result:
                    student = Student(result[0], result[1], result[2], result[3])
                    return student
                else:
                    return None
        except pymysql.Error as e:
            print(f"[ERROR] Error retrieving student: {e}")
            return None
        finally:
            pass

    def get_by_studentname(self, student_name):
        try:
            connection = self.conn
            with connection.cursor() as cursor:
                # SQL SELECT statement to retrieve a student by studentId
                sqlstr = f"SELECT * FROM student WHERE student_name like %s"
                params = ('%' + student_name + '%',)
                cursor.execute(sqlstr, params)
                results = cursor.fetchall()
                if results:
                    studentObjs = []
                    for row in results:
                        studentObjs.append(Student(row[0], row[1], row[2], row[3]))
                    return studentObjs
                else:
                    return None
        except pymysql.Error as e:
            print(f"[ERROR] Error retrieving student: {e}")
            return None
        finally:
            pass

    def get_all(self):
        try:
            connection = self.conn
            with connection.cursor() as cursor:
                # SQL SELECT statement to retrieve a student by studentId
                sql = "SELECT * FROM student"
                cursor.execute(sql)
                results = cursor.fetchall()
                if results:
                    studentObjs = []
                    for row in results:
                        studentObjs.append(Student(row[0], row[1], row[2], row[3]))
                    return studentObjs
                else:
                    return None
        except pymysql.Error as e:
            print(f"[ERROR] Error retrieving student: {e}")
            return None
        finally:
            pass

    def update(self, student):
        print(f"[DEBUG] student={student}")
        try:
            connection = self.conn
            with connection.cursor() as cursor:
                # SQL UPDATE statement to update a student by studentId
                sql = "UPDATE student SET student_name = %s, school_name = %s, grade = %s WHERE id = %s"
                values = (student.studentName, student.schoolName, student.gradeNo, student.studentId)
                cursor.execute(sql, values)
                connection.commit()
                return True
        except pymysql.Error as e:
            print(f"[ERROR] Error updating student: {e}")
            return False
        finally:
            pass

    def delete_by_id(self, student_id):
        try:
            connection = self.conn
            with connection.cursor() as cursor:
                # SQL DELETE statement to delete a student by studentId
                sql = "DELETE FROM student WHERE id = %s"
                cursor.execute(sql, student_id)
                connection.commit()
                return True
        except pymysql.Error as e:
            print(f"[ERROR] Error deleting student: {e}")
            return False
        finally:
            pass



