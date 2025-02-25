from datetime import datetime

def projectNameValidation(projectList):
    problems = []
    projectName = input('please input your project name: ')
    isProjectExist = list(x for x in projectList if x['projectName'] == projectName)
    if isProjectExist:
        problems.append('project name already exists')
    else:
        if len(projectName) < 3: problems.append('project name must be at least 3 characters long')
    if len(problems) > 0:
        for i in problems:
            print(i)
        return -1
    return projectName

def targetValidation():
    problems=[]
    target = input('please input your project target: ')
    if not target.isnumeric(): problems.append('target can only be numeric')
    if len(problems) > 0:
        for i in problems:
            print(i)
        return -1
    return target
def startDateValidation():
    problems = []
    startDate = input('please input your project start date in format dd-mm-yyyy: ')
    # if not startDate.isnumeric(): problems.append('start date can only be numeric')
    try:
        startDate = datetime.strptime(startDate, '%d-%m-%Y')
    except ValueError:
        problems.append('start date must be in the format dd-mm-yyyy')
        return -1
    if len(problems) > 0:
        for i in problems:
            print(i)
        return -1
    return startDate
def endDateValidation(startDate):
    problems = []
    endDate = input('please input your project end date in format dd-mm-yyyy: ')
    # if not endDate.isnumeric(): problems.append('end date can only be numeric')
    try:
        endDate = datetime.strptime(endDate, '%d-%m-%Y')
    except ValueError:
        problems.append('end date must be in the format dd-mm-yyyy')
        return -1
    if endDate < startDate: problems.append('end date must be after start date')
    if len(problems) > 0:
        for i in problems:
            print(i)
        return -1
    return endDate
def createProject(userLogged, projectList):
    projectDict = {}
    projectDict['projectName'] = projectNameValidation(projectList)
    projectDict['projectDescription'] = input('please input your project description: ')
    projectDict['projectOwner'] = userLogged['firstName'] + ' ' + userLogged['lastName']
    projectDict['projectOwnerEmail'] = userLogged['email']
    projectDict['projectTarget'] = targetValidation()
    if projectDict['projectTarget'] == -1: return -1
    projectDict['startDate'] = startDateValidation()
    if projectDict['startDate'] == -1: return -1
    projectDict['endDate'] = endDateValidation(projectDict['startDate'])
    if projectDict['endDate'] == -1: return -1
    print('project created successfully!')
    projectList.append(projectDict)
    return projectList

def viewProjects(projectList):
    for idx, project in enumerate(projectList):
        print(f'Project {idx+1}:', end=' ')
        print(f'{project["projectName"]}')
    return

def deleteProject(userLogged, projectList):
    userProjectsList = []
    for project in projectList:
        if project['projectOwnerEmail'] == userLogged['email']:
            userProjectsList.append(project)
    if not userProjectsList:
        print('you have no projects to delete')
        return
    viewProjects(userProjectsList)
    projectToDelete = input('please input the project name you want to delete: ')
    projectToDeleteVerify = list(x for x in userProjectsList if x['projectName'] == projectToDelete)
    if not projectToDeleteVerify:
        print('project doesnt exist')
        return
    projectList = list(x for x in projectList if x['projectName'] != projectToDelete)
    print('project deleted successfully')
    return projectList