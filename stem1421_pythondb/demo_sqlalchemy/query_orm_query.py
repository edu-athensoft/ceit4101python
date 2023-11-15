"""
Connecting to a database

pip install mysql-connector-python

"""

# import sqlalchemy as db
# engine = db.create_engine('dialect+driver://user:pass@host:port/db')

from sqlalchemy import create_engine, String, select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session

connection_string = "mysql+pymysql://root:my123@localhost:3306/stem1421_db2"
engine = create_engine(connection_string, echo=True)

connection = engine.connect()


class Base(DeclarativeBase):
    pass


class Student(Base):
    __tablename__ = "student"

    id: Mapped[int] = mapped_column(primary_key=True)
    student_name: Mapped[str] = mapped_column(String(20))
    school_name: Mapped[str] = mapped_column(String(30))
    grade: Mapped[str] = mapped_column(String(5))


with Session(engine) as session:
    for stuObj in session.scalars(select(Student)):
        print(stuObj.id, stuObj.student_name, stuObj.school_name, stuObj.grade)

