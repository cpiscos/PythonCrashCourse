# # 3-1
# names = ['rachel', 'wilfredo', 'kristina', 'christian']

# # 3-2
# for each_name in names:
#     print('Hello', each_name.title() + '!')

# # 3-3
# cars = ['mercedes', 'ferrari', 'rolls royce', 'tesla']
# for each_car in cars:
#     print('I would like to own a', each_car.title(), 'someday.')

# # 3-4
# guests = ['elon musk', 'linus pauling', 'jim simmons']
#
# def guest_messages():
#     print('\n')
#     for each_guest in guests:
#         print(each_guest.title() + ', you are invited to my dinner.')
#
#
# # guest_messages()
#
#
# # 3-5
# print('\nWho can\'t make it?')
# for n, each_guest in enumerate(guests):
#     print(str(n + 1) + '.', each_guest.title())
# declined = int(input()) - 1
# guests[declined] = input('\nReplace ' + guests[declined].title() + ' with?\n')
#
# guest_messages()
#
# # 3-6
# print('\nHey everyone, I found a bigger table! I\'ll invite more people.')
#
# new_invitees = ['ryan reynolds', 'beyonce', 'bruno mars']
# guests.insert(0, new_invitees[0])
# guests.insert(len(guests)//2, new_invitees[1])
# guests.append(new_invitees[-1])
#
# guest_messages()
#
# # 3-7
# print('\nSorry guys, the new table wont make it and I can\'t invite you all. I will un-invite randomly to make it fair.')
#
# import random
# for each_uninvited in range(len(guests)):
#     if len(guests) > 2:
#         uninvited = guests.pop(random.randint(0, len(guests) - 1))
#         print(uninvited + ', I have to un-invite you.')
#     else:
#         break
#
# guest_messages()
#
# for n in range(len(guests)):
#     del guests[0]
#
# print(guests)

# 3 - 8
places_to_visit = ['hong kong', 'tokyo', 'rome', 'london', 'new york']
print(places_to_visit)
print(sorted(places_to_visit))
print(places_to_visit)
print(sorted(places_to_visit, reverse=True))
print(places_to_visit)
places_to_visit.reverse()
print(places_to_visit)
places_to_visit.reverse()
print(places_to_visit)
places_to_visit.sort()
print(places_to_visit)
places_to_visit.sort()
print(places_to_visit)
