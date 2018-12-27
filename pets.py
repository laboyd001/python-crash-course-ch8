#positional arguments

def describe_pet(animal_type, pet_name):
    """Display info about pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet('cat', 'grits')

#multiple function calls

describe_pet('dog', 'boba')