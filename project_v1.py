#Beginning of internship Python project.
def menu():
    choice = ''
    while choice != 'succeed' and choice == '':
        choice = input('What will you do in this internship?')
    if choice == 'succeed':
        print('Yes you will!')
    
menu()
