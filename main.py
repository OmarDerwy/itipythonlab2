from registeration import login,register
from projects import createProject, viewProjects, deleteProject

def main(userLogged, userList, projectList, userIn):
    while userIn:
        if not userLogged:
            userChoice = input('Welcome to our crowdfunding CLI app! Please select a choice below:\n1- Login\n2- Register\n3- exit\n\n')
            userChoice = userChoice.lower()
            match userChoice:
                case '1' | 'login':
                    userLogged = login(userList)
                case '2' | 'register':
                    userList = register(userList)
                case '3' | 'exit':
                    userIn = False
        else:
            userChoice = input('what do you wanna do in our site?\n1- create project\n2- view projects\n3- delete project\n4- exit\n\n')
            userChoice = userChoice.lower()
            match userChoice:
                case '1' | 'create project':
                    createProject(userLogged, projectList)
                case '2' | 'view projects':
                    viewProjects(projectList)
                case '3' | 'delete project':
                    projectList = deleteProject(userLogged, projectList)
                case '4' | 'exit':
                    userIn = False
                



if __name__ == '__main__':
    userIn = True
    projectList = [{
        'projectName': 'demo',
        'projectDescription': 'demo',
        'projectOwner': 'demo',
        'projectOwnerEmail': 'demo',
        'projectTarget': 1000,
        'startDate': '01-01-2025',
        'endDate': '01-01-2026'
    }]
    userList = [{
        'firstName': 'demo',
        'lastName': 'demo',
        'email': 'demo',
        'password': 'demo',
        'phoneNumber': '01234567890'
    }]
    userLogged = None
    main(userLogged, userList, projectList, userIn)
