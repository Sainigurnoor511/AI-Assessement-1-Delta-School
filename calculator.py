def calculator():
    print("Please type in the math operation you would like to complete:")
    print("+ for addition")
    print("- for subtraction")
    print("* for multiplication")
    print("/ for division")
    operation = input()

    number_1 = int(input("Please enter the first number: "))
    number_2 = int(input("Please enter the second number: "))

    if operation == "+":
        print(f"{number_1} + {number_2} = {number_1 + number_2}")

    elif operation == "-":
        print(f"{number_1} - {number_2} = {number_1 - number_2}")

    elif operation == "*":
        print(f"{number_1} * {number_2} = {number_1 * number_2}")

    elif operation == "/":
        print(f"{number_1} / {number_2} = {number_1 / number_2}")

    else:
        print("Invalid operator")

    again() #create a function to ask if the user wants to calculate again


def again():
    print("Do you want to calculate again?")
    print("Type Y for yes or N for no.")
    calc_again = input()

    if calc_again.upper() == "Y":
        calculate()
    elif calc_again.upper() == "N":
        print()
    else:
        again()

calculator()