def calculator():
    print("Welcome to Calculator")
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        print("\nChoose an operation:")
        print("1.Addition")
        print("2.Subtraction")
        print("3.Multiplication")
        print("4.Division")
        choice = input("Enter your choice:")
        if choice == '1':
            result = num1 + num2
            print(f"\nResult: {num1} + {num2} = {result}")
        elif choice == '2':
            result = num1 - num2
            print(f"\nResult: {num1} - {num2} = {result}")
        elif choice == '3':
            result = num1 * num2
            print(f"\nResult: {num1} * {num2} = {result}")
        elif choice == '4':
            if num2 != 0:
                result = num1 / num2
                print(f"\nResult: {num1} / {num2} = {result}")
            else:
                print("\nError:Cannot divide by zero")
        else:
            print("\nInvalidchoice.")
    except ValueError:
        print("\nError:Enter valid number")
calculator()
