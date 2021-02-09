# class NameTooShortError (Exception):
#     pass
#
# class MustContainAtSymbolError  (Exception):
#     pass
#
# class InvalidDomainError  (Exception):
#     pass

import exeption

def name_validate(email):
    name = email.split('@')[0]
    if len(name)<4:
        raise exeption.NameTooShortError (f'Name must be more than 4 characters')
    return True

def symbol_validate(email):
    if not '@' in email:
        raise exeption.MustContainAtSymbolError (f'Email must contain @')
    return True

def domain_validate(email):
    domain = email.split ( '.' )[-1]
    domain_lst = ['com', 'bg', 'org', 'net']
    if domain not in domain_lst:
        raise exeption.InvalidDomainError (f'Domain must be one of the following: .com, .bg, .org, .net')
    return True

email = input()
while True:
    if not email:
        break
    if domain_validate(email) and symbol_validate(email) and name_validate(email):
        print("Email is valid" )
    email = input ()

