from datetime import date
from models import Student, db
import logging
import logging.config
from peewee import Model
# logging.basicConfig(level=logging.DEBUG, format='%(name)s - %(levelname)s - %(message)s')
logging.config.fileConfig(fname='app.conf', disable_existing_loggers=False)
logger = logging.getLogger(__name__)


def create_student(student):
    try:
        student.name = str(input('Enter first name: '))
        student.last_name = input('Enter last name: ')
        student.year_birth = input('Enter birth date(yyyy.mm.dd): ')
        student.address_residence = input('Enter address residence: ')
        student.year_admission = input('Enter year admission(yyyy.mm.dd): ')
        student.group = input('Enter group: ')
        student.average_score = input('Enter average score: ')
        student.save()
        logger.info('Successful with creating student with id %s', student.id)
    except BaseException as e:
        logger.error('Invalid creating student', e)


def get_student_by_id(student):
    try:
        id = input('Enter id')
        student_by_id = student.get_by_id(id)
        logger.info('Successful get student with id %s', id)
        return student_by_id
    except BaseException as e:
        logger.error('Invalid entering id %s', e)


def read_all_students(student):
    try:
        students = []
        for student in student.select():
            students.append(student)
        logger.info('Successful get all students')
        return students
    except BaseException as e:
        logger.error('Invalid select * students %s', e)


def update_student_by_id(student:Model):
    try:
        id = int(input('Enter id: '))
        student = student.get_by_id(id)
        student.name = str(input('Enter first name: '))
        student.last_name = input('Enter last name: ')
        student.year_birth = input('Enter birth date(yyyy.mm.dd): ')
        student.address_residence = input('Enter address residence: ')
        student.year_admission = input('Enter year admission(yyyy.mm.dd): ')
        student.group = input('Enter group: ')
        student.average_score = input('Enter average score: ')
        student.save()
        logger.info('Successful update student by id %s ', id)
        return student
    except BaseException as e:
        logger.error('Invalid entering id %s', e)


def delete_student_by_id(student):
    try:
        id = int(input('Enter id: '))
        student.delete_by_id(id)
        logger.info('Successful deleting student with id %s', id)
    except BaseException as e:
        logger.error('Invalid entering id %s', e)


def main():
    student = Student()
    switcher = {
        1: create_student,
        2: get_student_by_id,
        3: read_all_students,
        4: update_student_by_id,
        5: delete_student_by_id,

    }
    while True:
        cmd = int(input('1 - create student\n'
                        '2 - read students\n'
                        '3 - read all students\n'
                        '4 - update student\n'
                        '5 - delete student\n'
                        'Enter command:'))
        response = switcher[cmd](student)
        if type(response) == list or type(response) == tuple:
            for row in response:
                print(row)
        else:
            print(response)


if __name__ == "__main__":
    main()
