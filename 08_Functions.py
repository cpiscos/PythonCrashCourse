magicians = ['houdini', 'david baine']


def make_great():
    for n,each_magician in enumerate(magicians):
        magicians[n] = 'The Great ' + each_magician.title()

def show_magicians():
    [print(x.title()) for x in magicians]

show_magicians()
make_great()
show_magicians()