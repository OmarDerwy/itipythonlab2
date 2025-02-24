def mobileValidation():
    problems = []
    mobileNumber = input('Please ya user input your phone number: ')
    mobileNumber=mobileNumber.replace("+", "")
    if mobileNumber.startswith('2'):
        mobileNumber=mobileNumber[1:]
    if not mobileNumber.isnumeric(): problems.append('number can only be numeric')
    if mobileNumber[:3] not in ['010','011','012','015']: problems.append('phone number can only be vodafone, etisalat, we, or orange')
    if len(mobileNumber) != 11: problems.append('Number can only be 11 digits long')        

    if len(problems) > 0:
        for i in problems:
            print(i)
        return -1
    else:
        print('number verified')
        return mobileNumber

        
def passwordValidation():
    password = input('please input password ya user: ')
    problems = []
    if not password:
        problems.append('please yasta dont leave the box empty yasta')
    else:
        if password.lower() == password: problems.append('Please have at least one upper case letter')
        # if len(password) < 8: problems.append('Please have the password be at least 8 characters long')
        if password.isalpha(): problems.append()
        flag = False
        for i in password:
            if i.isnumeric():
                flag=True
        if flag == False: problems.append('please have at least one digit in the password')

    if len(problems) > 0:
        for i in problems:
            print(i)
        return -1
    else:
        confirmPassword = input ('please confirm password ya user: ')
        if password != confirmPassword:
            return -1
        else:
            print('thank you!')
            return password

def emailValidation():
    a = input('Please input a valid email ya user: ')
    problems = []
    if a.count('@') != 1:
        problems.append('you forgot the @ yasta')
    else:
        atPosition = a.index('@')
        if a[atPosition:].count('.') != 1:
            problems.append('you forgot the . after the @ yasta')
    if len(problems) > 0:
        for i in problems:
            print(i)
        return -1
    else:
        print('thank you for this good validated email yasta')
        return a

def login(userList:list):
    if not userList:
        print('oops, we have no users yet haha')
    else:
        trials = 0
        emailInput = input('Please input your email ya user: ')
        emailSearch:list = list(x for x in userList if x['email'] == emailInput)
        if not emailSearch:
            print('this email doesnt exist yasta register and come back.')
            return False
        while trials < 3:
            passwordInput = input('Please input your password ya bro: ')
            if passwordInput == emailSearch[0]['password']:
                return emailSearch[0]


def register(userList:list):
    userDict = {}
    userDict['firstName'] = input('please input your first name: ')
    userDict['lastName'] = input('please input your last name: ')
    userDict['email'] = emailValidation()
    if userDict['email'] == -1: return -1
    userDict['password'] = passwordValidation()
    if userDict['password'] == -1: return -1
    userDict['mobilePhone'] = mobileValidation()
    if userDict['mobilePhone'] == -1: return -1
    print('user has been validated successfully. user is being added to the database...')
    userList.append(userDict)

