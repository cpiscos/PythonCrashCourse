detail = {}
print('to exit, type: cancel')
cont='y'
cont1='y'

while cont == 'y':
    name = input('Person\'s name?: ')
    age = input(str(name)+'\'s age?: ')
    hair = input(str(name)+'\'s hair color?: ')
    detail[name]=[age, hair]
    cont=input('Add another person?: [y/n]')
    if cont == 'n':
        break

while cont1 == 'y':
    namereq = input('Who would you like to know about?: ')
    option = input('If you\'d like to know about their age enter 1\nIf you\'d like to know about their hair color enter 2\n')
    if option == '1':
        print(detail[namereq][0])
    elif option == '2':
        print(detail[namereq][1])
    else:
        print('invalid')
    cont1=input('Would you like to know more?: [y/n]')
    if cont1 == 'n':
        break    
