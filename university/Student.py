import datetime


class Student():#brezinys, blueprint, liejimp formele,sablonas, instrukcija koks turi buti objektas
    def __init__(self,name = "", surname = "", birth_date = datetime.date.today(), studies = []):#konstruktorius
        self.name = name
        self.surname = surname
        self.birth_date = birth_date
        self.studies = studies

    def __str__(self):
        return f'{self.name} {self.surname}, {self.birth_date}, \n {self.studies}'