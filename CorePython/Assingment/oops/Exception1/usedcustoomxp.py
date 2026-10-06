class Userdefine(Exception):
    pass
try:
    no = int(input("Enter the number: "))
    if no < 0:
        raise Userdefine("Number should be greater than 0")
    print("I am good")
except Userdefine as u:
    print("Custom Exception:", u)
except ValueError:
    print("Please enter a valid integer.")