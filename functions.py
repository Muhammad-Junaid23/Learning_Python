# we will write some python functions

def user_name(first_name, last_name):
    print(f"Hi {first_name} {last_name}")


def greetings():
    print("Welcome to python crash course")


user_name("Unknown", "X")
greetings()


# Types of functions
# -- functions that perform a task  (like the above one)
# -- functions that calculate and return a value  (like the round(1.34))

def perform_addition(num1, num2):
    return num1 + num2


add_result = perform_addition(4, 6)
print(f"Result of Addition : ", add_result)
print(f"Result of Addition : ", perform_addition(45, 7))
print(f"Result of Addition : ", perform_addition(num1=25, num2=52))

# passing multiple arguments to function


def multiple_numbers(*tupple):
    total = 1
    for x in tupple:
        total *= x
    return total


print('Result of mulitplying numbers : ', multiple_numbers(2, 1, 5, 3, 6, 9))

# file handling
# messgae = "Welcome to python crash course"
# file = open("greeting.txt", 'w')
# file.write(messgae)
