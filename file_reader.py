filename = 'pi_one_mil_digits.txt'

with open(filename) as file_object:
    lines = file_object.read()
    # print(lines.rstrip())

pi_string = ''
for line in lines:
    pi_string += line.rstrip()

print(pi_string[:51])
print(len(pi_string))
birthday =