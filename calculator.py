import art
print(art.calculator_art)

# Addition
def add(a,b):
    return a + b

# subtraction
def subtract(a,b):
    return a-b

# Multiplication
def multiply(a,b):
    return a*b

# Division
def divide(a,b):
    return a/b

iscontinue = True

while iscontinue:
    first_num = int(input("what is the first number? "))
    # operation_list = ["+","-","*","/"]
    operation_dict = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide,
    }
    for key in operation_dict:
        print(key)

    o = input("pick an operation")
    second_number = int(input("what is the next number? "))
    print(operation_dict[o](first_num,second_number))

    i = input("Press Y to continue else press any key").lower()
    if i == "y":
        pass
    else:
        iscontinue = False
