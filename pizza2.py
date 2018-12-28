#making modules

def make_pizza2(size, *toppings):
    """Summarize teh pizza we are about to make."""
    print("\nMaking a " + str(size) + "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)

