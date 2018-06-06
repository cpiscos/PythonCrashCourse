cats = ['garfield', 'king', 'larry']
dogs = ['snow', 'max', 'john']
filenames = ['cats.txt', 'dogs.txt']


def read_cats_dogs():
    for filename in filenames:
        try:
            file = open(filename)
            print(file.read().title())
        except FileNotFoundError:
            pass


def write_cats_dogs():
    with open(filenames[0], 'w') as c_obj:
        for cat in cats:
            c_obj.write(cat + '\n')

    with open(filenames[1], 'w') as d_obj:
        for dog in dogs:
            d_obj.write(dog + '\n')
# write_cats_dogs()
# read_cats_dogs()
