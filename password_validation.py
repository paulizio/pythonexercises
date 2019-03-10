import re

''' A strong password is defined as one that is at least eight characters long,
    contains both uppercase and lowercase characters,and has at least one digit.'''

def password_validation(password):

    #Password validation criteria
    hasLowerCase=re.compile(r'[a-z]+')
    hasUpperCase=re.compile(r'[A-Z]+')
    hasDigit=re.compile(r'\d+')
    hasLength=re.compile(r'.{8,}')

    #Response messages
    weak='You have entered a weak password. Please try again.'
    strong='Your password is strong.'
    insert_new='Insert new password: '

    #Validate password. Loop until strong password.
    flag=True
    while flag:
        if hasLowerCase.search(password)==None:
            print(weak)
            password=input(insert_new)
            continue
        elif hasUpperCase.search(password)==None:
            print(weak)
            password=input(insert_new)
            continue
        elif hasDigit.search(password)==None:
            print(weak)
            password=input(insert_new)
            continue
        elif hasLength.search(password)==None:
            print(weak)
            password=input(insert_new)
            continue
            
        else:
            print(strong)
            flag=False
            break
            

pw=input('Enter a password: ')
password_validation(pw)


