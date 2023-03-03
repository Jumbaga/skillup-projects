
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

#Populating projects dictionary keys with project names and initializing value at None
for project_name in project_names:
    projects[project_name] = []

#Populating projects dictionary values with developer names checking against the projects on developers dictionary,
#also filtering duplicates
for developer_name in developer_names:
    for project_name in developers[developer_name]:
        if developer_name not in projects[project_name]:
            projects[project_name].append(developer_name)

print(projects)
             


