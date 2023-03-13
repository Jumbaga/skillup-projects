from datetime import date
from functools import total_ordering

#Person class contructor, with name, surname, UID, municipality and DOB as dependencies
class Person:
    def __init__(self, name, surname, UID, municipality, DOB):
        self.name = name
        self.surname = surname
        self._UID = UID
        self.municipality = municipality
        self.DOB = DOB

#Class Getters    
    def get_name(self):
        return self.name
    def get_surname(self):
        return self.surname
    def get_UID(self):
        return self._UID
    def get_municipality(self):
        return self.municipality
    def get_DOB(self):
        return self.DOB

#Overriden less then to avaluate DOB when comparing Person objects
    def __lt__(self, other):
        return self.DOB < other.DOB

#Class Setters    
    def set_name(self, name):
        self.name = name
    def set_surname(self, surname):
        self.surname = surname
    def set_municipality(self, municipality):
        self.municipality = municipality
        
#Data validation for UID, needs to be an 8 digit integer
    def set_UID(self):
        new_UID = input('Enter a portuguese UID, with 8 integers ')
        if  new_UID.isdigit() and len(str(new_UID)) == 8:
            print(f'Old UID was {self._UID}, new one is {new_UID}.')
            self._UID = new_UID
        else:
            raise Exception('Invalid format, provide a portuguese UID, with 8 integers')
#Data validation for DOB, needs to be a date in YYYY-MM-DD format, and cannot be later than current date        
    def set_DOB(self):
        date_input = input('Enter a date in YYYY-MM-DD format ')
        year, month, day = map(int, date_input.split('-'))
        new_DOB = date(year, month , day)
        if date.today() >= new_DOB:
            print(f'Old DOB was {self.DOB}, new one is {new_DOB}.')
            self.DOB = new_DOB
        else:
            raise Exception('Invalid format, provide a date in YYYY-MM-DD format '
                            'or the date you provided is in the future.')

#Creating 5 instances of Person
vitor = Person('Vitor', 'Amaral', 13569134, 'Lisbon', date(1990, 1, 18))
mariana = Person('Mariana', 'Dias', 12345612, 'Lisbon', date(1991, 7, 15))
hipolito = Person('Hipolito', 'Lopes', 12344321, 'Covilha', date(1999, 5, 3))
domingos = Person('Domingos', 'Coelho', 12332112, 'Lisbon', date(1993, 3, 17))
fabio = Person('Fabio', 'Salome', 12121212, 'Leiria', date(1990, 4, 25))

#Putting them on a List
my_peeps_lst = [mariana, hipolito, domingos, fabio, vitor]

def get_oldest():
    #Sorting persons by DOB (see less override above) and selecting the first element (oldest DOB)
    oldest = sorted(my_peeps_lst)[0]
    #Printing oldest person name, surname and DOB
    print(f'The oldest person is {oldest.name} {oldest.surname}, born on {oldest.DOB}.')

get_oldest()

    