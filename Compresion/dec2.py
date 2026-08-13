def decorator1(fun):

    def wrapper(*args, **kwargs):

        print("Before Function")

        fun(*args, **kwargs)

        print("After Function")

    return wrapper


@decorator1
def add(a, b):
    print("Addition =", a + b)


@decorator1
def login():
    print("Login Successful")


@decorator1
def emp(id, name, salary):
    print(id, name, salary)


add(10, 20)

print("----------------")

login()

print("----------------")

emp(101, "Pradip", 50000)