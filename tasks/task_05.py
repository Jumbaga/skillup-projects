from task_04 import Person, my_peeps_lst
import random

#Worker class extendeds from Person so it has the same dependencies and more: occupation, monthly salary and
#years of service
class Worker(Person):
    def __init__(self, name, surname, UID, municipality, DOB, occupation, monthly_salary, years_of_service):
        super().__init__(name, surname, UID, municipality, DOB)
        self.occupation = occupation
        self.__monthly_salary = monthly_salary
        self.years_of_service = years_of_service
#Function returns a tupple in the format specified of (name, date of birth, years of service, annual income) and
#its provided by acessing the instance properties. Annual income is calculated by simply multiplaying monthly salary by 12.
    def annual_income(self):
        return (self.name, self.DOB, self.years_of_service, self.__monthly_salary * 12)
#Function to create a list of workers sorted by their annual income, went ahead a made also lists sorted by years of service
#and date of birth, made the method have a list as dependency so I could use the list of instances created on the previous task
def sort_by_income(prs_lst):
    worker_lst = []
    occup_lst = ["Developer", "Telecom Engineer", "HR", "QA", "Marketing"] #List of potenial occupations
    salary_lst = [*range(1200, 2200, 200)] #List of salaries ranging from 1200 to 2000, with a 200 step, resulting in a 5 element list
    yos_lst = [*range(1,6)] # List of years of serving ranging from 1 to 5 resulting in a 5 element list
    
    for person in prs_lst:
        
        #Selecting random elements from the lists above and removing them from the lists so there are no duplicates
        occupation = occup_lst.pop(random.randrange(len(occup_lst)))
        salary = salary_lst.pop(random.randrange(len(salary_lst)))
        years_of_service = yos_lst.pop(random.randrange(len(yos_lst)))

        #Using the list of Person instances to fullfill the __init__ dependencies of the Worker class, specifically,
        #Person instance properties can be used to the satisfy the super() dependencies and occupation, salary and
        #years of service are chosen randomly from the above lists.
        worker_lst.append(Worker(person.name, person.surname, person._UID, person.municipality, person.DOB, 
                                 occupation, salary, years_of_service))
    
    #Using Python native sorted to sort the lists as specified, used lambda key function to specify what properties or values
    #to use as comparisson
    income_sorted_lst = sorted(worker_lst, key = lambda worker: worker.annual_income()[3], reverse=True)
    yos_sorted_lst = sorted(worker_lst, key = lambda worker: worker.years_of_service, reverse=True)
    #Because __lt__ (less then) was overriden on parent class Person, it will always compare Persons and Workers(by extension)
    #by DOB (date of birth) so no need to specify a lambda key function
    DOB_sorted_lst = sorted(worker_lst)

    #Iterating through the 3 lists to check if order is correct after sorting and printing relevant info
    for worker in income_sorted_lst:
        print(f'{worker.name} has the annual income of {worker.annual_income()[3]}. [MAX IS 24K]')
    
    for worker in yos_sorted_lst:
        print(f'{worker.name} has worked for {worker.years_of_service} years. [MAX IS 5]')
    
    for worker in DOB_sorted_lst:
        print(f'{worker.name} was born on {worker.DOB.year}-{worker.DOB.month}-{worker.DOB.day}. [OLDEST DATE 1990-1-18]')

#Funcion call, passed list from task_04 as argument simply to avoid having to re-write so many properties when I could re-use them    
sort_by_income(my_peeps_lst)