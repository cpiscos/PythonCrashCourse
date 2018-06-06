import json

filename = 'favorite_number.json'


def get_stored_number():
    """Gets stored number in filename"""
    try:
        with open(filename) as f_obj:
            favorite_number = json.load(f_obj)
        return favorite_number
    except FileNotFoundError:
        return None
    else:
        return favorite_number


def store_new_number():
    """Stores new number"""
    new_number = input("What is your favorite number? ")
    with open(filename, 'w') as f_obj:
        json.dump(new_number, f_obj)
    return new_number


def favorite_number():
    """Favorite number!!!"""
    number = get_stored_number()
    if number:
        print("Your favorite number is " + number + "!")
    else:
        new_number = store_new_number()
        print("We'll store your favorite number: " + new_number)


favorite_number()
