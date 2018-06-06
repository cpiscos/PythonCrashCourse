filename = 'guest.txt'

open(filename, 'w')
with open(filename, 'a') as guest_list:
    while True:
        guest = input("Guest's name? ")
if guest != 'exit':
    guest_list.write(guest + '\n')
else:
    break
