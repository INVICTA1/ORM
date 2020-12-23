import peewee

db = peewee.MySQLDatabase('orm', user='admin', password='admin',
                          host='127.0.0.1', port=3306)


class Student(peewee.Model):
    name = peewee.CharField()
    last_name = peewee.CharField()
    year_birth = peewee.DateField()
    address_residence = peewee.CharField()
    year_admission = peewee.DateField()
    group = peewee.IntegerField()
    average_score = peewee.IntegerField()

    class Meta:
        database = db

    def __str__(self):
        return str(self.id) + ' ' + self.name + ' ' + self.last_name + ' ' + str(self.year_birth) + ' ' + self.address_residence + ' ' + str(self.year_admission) + ' ' + str(self.group) + ' ' + str(self.average_score)


if __name__ == "__main__":
    try:
        Student.create_table()
    except peewee.OperationalError as e:
        print("Table Student already exists!")
