from datetime import date
from models import Student


def create_student(name, last_name, year_birth, address_residence, year_admission, group, average_score):
    student = Student(name=name, last_name=last_name, year_birth=year_birth, address_residence=address_residence,
                      year_admission=year_admission, group=group, average_score=average_score)
    student.save()



def get_data_from_student():
    student = Student.get(Student.name == 'Mask')
    print(student)

if __name__ == "__main__":
    create_student('Mask', 'Ilon', date(1998, 12, 20), 'silikonavata dolina', 2014, 78964, 5)
    get_data_from_student()
