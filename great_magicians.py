#Start with a copy of the program from 8-9.  Write a function called make_great() that modifies the list of magicians by adding the phrase the great to each name.  Call the show_magicians() to see that the list has been modified.

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

magicians = ['houdini', 'penn and teller', 'david blaine']
show_magicians(magicians)

print("\n")
make_great(magicians)
show_magicians(magicians)
