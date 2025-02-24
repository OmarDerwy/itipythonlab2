from registeration import login,register
def main(userLogged, userList, userIn):
    while userIn:
        if not userLogged:
            userChoice = input('Welcome to our crowdfunding CLI app! Please select a choice below:\n1- Login\n2- Register\n3- exit\n\n')
            userChoice = userChoice.lower()
            match userChoice:
                case '1' | 'login':
                    userLogged = login(userList)
                case '2' | 'register':
                    register(userList)
                case '3' | 'exit':
                    userIn = False
        else:
            userChoice = input('what do you wanna do in our site?\n1- exit\n\n')
            


if __name__ == '__main__':
    userIn = True
    userList = [{
        'firstName': 'demo',
        'lastName': 'demo',
        'email': 'demo',
        'password': 'demo',
        'phoneNumber': '01234567890'
    }]
    userLogged = None
    main(userLogged, userList, userIn)
