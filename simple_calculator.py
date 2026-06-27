while True:
    print("simple_calculator")

    number1 = float(input("first number:"))
    operator = input("enter operator ( + , - , * , / ):")
    number2 = float(input("second number:"))

    if operator == "+":
        print("Result:" , number1 + number2)

    elif operator == "-":
        print("Result:" , number1 - number2)

    elif operator == "*":
        print("Result:" , number1 * number2)

    elif operator == "/":
        if number2 != 0:
            print("Result:" , number1 / number2)
        else:
            print("please don't enter zero. / can't divide by zero!")

    else:
        print("invalid operator!")

    again = input("continue? (yes/no):")

    if again.lower() != "yes":
        print("have a good day/night!")
        break