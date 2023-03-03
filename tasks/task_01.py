
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
        developers[dev_name]=dev_projects
        number_of_developers = len(developers.keys())
        print(f'Number of developers changed from {number_of_developers - 1} to {number_of_developers}')
        return number_of_developers
    else:
        print("Incorrect format, provide a name and a list, or, the developer name provided already exists")

#Checking if correct format and not duplicate is added    
add_developer("Tito",["Company website", "Fashion store website"])
#Checking if will block duplicate developer names
add_developer("Tito",["Project Ocean"])
#Checking if will block duplicate and incorrect format for the 2nd argument
add_developer("Tito", 5)
#Checking if will block incorrect format for the 1st argument
add_developer(5,["Company website"])
#Checking if will block incorrect format for the 1st and 2nd arguments
add_developer(10,"purple")

