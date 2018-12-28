#start with the program from 8-10, but this time use a copy of the magcian list in the function call

def show_magicians(magicians):
    """show the name of each magician."""
    for magician in magicians:
        print(magician.title())

def make_great(magicians):
    """Make the magicians great!"""
    great_magicians = []

    while magicians:
        magician = magicians.pop()
        great_magician = magician + ' the Great'
        great_magicians.append(great_magician)

    for great_magician in great_magicians:
        magicians.append(great_magician)
    return magicians

magicians = ['houdini', 'penn and teller', 'david blaine']
show_magicians(magicians)

print("\nGreat Magicians:")
great_magicians = make_great(magicians[:])
show_magicians(great_magicians)

print("\nOriginal Magicians:")
show_magicians(magicians)