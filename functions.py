def user():
    print("""Calculator in Python using functions:\n""")
def interface():
    while True:
        number1 = float(input("Enter first number: "))
        number2 = float(input("Enter second number: "))

        operation = int(input("""Choose an Operation(between 1-4): 
        1. Addition
        2. Subtraction
        3. Multiplication
        4. Division\n
        Operation: """))

        if operation == 1:
            sum = number1 + number2
            print(f"Answer: {number1} + {number2} = {sum}")
        elif operation == 2:
            difference = number1 - number2
            print(f"Answer: {number1} - {number2} = {difference}")
        elif operation == 3:
            product = number1 * number2
            print(f"Answer: {number1} * {number2} = {product}")
        elif operation == 4:
            while True:
                if number2 != 0:
                    quotient = number1 / number2
                    print(f"Answer: {number1} / {number2} = {quotient}")
                    break
                else:
                    print("Can't divide by zero")
                    break
        else:
            print("Invalid choice. Please choose from the Available Operations.")

        choice = input("Do you want to continue? [Y/N]: ")
        if choice.lower() != 'y':
            print("Arigato!")
            break

user()
interface()