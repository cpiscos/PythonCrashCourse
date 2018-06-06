filename = 'pi_one_mil_digits.txt'

with open(filename) as file_object:
    lines = file_object.read()
    # print(lines.rstrip())

pi_string = ''
for line in lines:
    pi_string += line.rstrip()

print(pi_string[:51])
print(len(pi_string))
birthday = input('Input your birthday in the form of mmddyy: ')
if birthday in pi_string:
    print('Your birthday appears in the first million digits of pi!')
else:
    print('Your birthday does not appear in the first million digits of pi.')
