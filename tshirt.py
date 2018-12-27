#create a function that takes an argument of size and text.  the function should print a sentence summarizing the size and message.

# def tshirt(size, text):
#     """Display shirt info"""
#     print("\nMy shirt size is " + size + ".")
#     print("I want it to say: " + text + ".")
# tshirt('medium', 'I love cats')
# tshirt(size = 'small', text = "I'm hungry")

#default value

def tshirt(size = 'large', text = 'I love python'):
    """Display shirt info"""
    print("\nMy shirt size is " + size + ".")
    print("I want it to say: " + text + ".")
tshirt()
tshirt(size = 'medium')
tshirt(size = 'medium', text = 'Fly a kite')

