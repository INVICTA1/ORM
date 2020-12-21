import peewee
import datetime
import databases

db = peewee.SqliteDatabase('people.db')

class Student(peewee.Model):
    name = peewee.CharField()
    last_name = peewee.CharField()
    year_birth = peewee.DateTimeField()
    address_residence = peewee.CharField()
    year_admission = peewee.DateTimeField()
    group = peewee.IntegerField()
    average_score = peewee.IntegerField()

    class Meta:
        database  = db




if __name__ == "__main__":
    try:
        Student.create_table()
    except peewee.OperationalError:
        print("Table Student already exists!")

