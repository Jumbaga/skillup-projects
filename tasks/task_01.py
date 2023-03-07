import numpy as np

#Dictionary of developers and respective projects, key is developer name, value is a list of project names

developers = {"Marshal": ["Company website", "Animal recognition", "Fashion store website"],
"Ted": ["Plants watering system", "WHAT", "Animal recognition", "Food recognition"],
"Monica": ["NEXT website", "Fashion store website"], 
"Phoebe": ["WHAT", "Company website", "NEXT website"]}

#Step one of the task, dictionary of the projects and developers, key is project name, value is a list of project names

#Creating an empty list for project names
project_names = []

#Flattening the list of lists returned by the developer dictionary values using a list comprehension
project_list = [project_name for project_list in developers.values() for project_name in project_list]

#Populating the project_names list with a list comprehension of project_list to filter duplicates
[project_names.append(project_name) for project_name in project_list if project_name not in project_names]

#Creating list for developer names from the developers dictionary keys
developer_names = list(developers.keys())

#Creating an empty projects dictionary
projects = {}

#Populating projects dictionary keys with project names
for project_name in project_names:
    projects[project_name] = []

#Populating projects dictionary values with developer names checking against the projects on developers dictionary,
#also filtering duplicates
for developer_name in developer_names:
    for project_name in developers[developer_name]:
        if developer_name not in projects[project_name]:
            projects[project_name].append(developer_name)

#Step two of the task creating a set with project names (I had already made this in step one without using a set, filtering the results)
project_set = set(project_list)

#Step three of the task, changing the names on the project list to a format of ASPIRE_projectname
aspire_projects = ['ASPIRE_' + projectname for projectname in project_names]

#Step four of the task, a function has developer name and a list of projects as dependencies and adds it to the developers dictionary
#and returns the new total number of developers, using type safety and filtering duplicates
def add_developer(dev_name, dev_projects):
    if type(dev_name) is str and type(dev_projects) is list and dev_name not in developers.keys():
        developers[dev_name] = dev_projects
        number_of_developers = len(developers.keys())
        print(f'Number of developers changed from {number_of_developers - 1} to {number_of_developers}')
        return number_of_developers
    else:
        print("Incorrect format, provide a name and a list, or, the developer name provided already exists")

#Receives a project name str and a time/revenue tupple, updates de projects on developers
#dictionary to include the time/revenue on the respective projects
def add_time_and_revenue(project_name, *args):
    for time, revenue in args:
        tupple_values = time, revenue
        for dev_name in developers.keys():
            if project_name in developers[dev_name]:
                value = developers[dev_name].index(project_name)
                developers[dev_name][value] = (project_name, tupple_values)
                #print(developers)

add_time_and_revenue("Company website",("240h", 5000))
add_time_and_revenue("Food recognition",("300h", 8000))
add_time_and_revenue("Animal recognition",("450h", 12000))
add_time_and_revenue("NEXT website",("600h", 25000))
add_time_and_revenue("WHAT",("150h", 7500))
add_time_and_revenue("Plants watering system",("30h", 2000))
add_time_and_revenue("Fashion store website",("750h", 5000))

def print_dev_revenues():
    book_keeping_dict = {}
    dev_revenue_dict = {}
    
    for project in developers.values():
        for project_name in project:
            if project_name in book_keeping_dict.keys():
                book_keeping_dict[project_name] += 1
            else:
                book_keeping_dict[project_name] = 1
    
    for dev_name in developers.keys():
        dev_revenue_dict[dev_name] = []
        for project_name in book_keeping_dict.keys():
            if project_name in developers[dev_name]:
                number_devs_in_proj = book_keeping_dict[project_name]
                total_project_hours = int(developers[dev_name][developers[dev_name]
                        .index(project_name)][1][0][:-1])
                total_project_expense = developers[dev_name][developers[dev_name]
                                                            .index(project_name)][1][1]
                project_hours = int(total_project_hours/number_devs_in_proj)
                dev_proj_income = int(total_project_expense/number_devs_in_proj)
                dev_revenue_dict[dev_name].append(dev_proj_income)
        dev_income_per_hour = sum(dev_revenue_dict[dev_name])/project_hours      
        print(f'Developer {dev_name} earns {dev_income_per_hour} euros per hour')
                         
print_dev_revenues()


        

