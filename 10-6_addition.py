while True:
    a = input('First number to add: ')
    b = input('Second number to add: ')
    try:
        c = float(a) + float(b)
        print(c)
    except ValueError:
        print("Value must be a number!")
