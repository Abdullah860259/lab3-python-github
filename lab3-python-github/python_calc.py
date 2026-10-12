def show_instructions():
    print("=" * 40)
    print("        PYTHON CALCULATOR - HELP")
    print("=" * 40)
    print("1. First choose an operation by entering its number:")
    print("     1  Addition (+)")
    print("     2  Subtraction (-)")
    print("     3  Multiplication (*)")
    print("     4  Division (/) (the second number cannot be 0)")
    print("2. Then enter the first number when prompted.")
    print("3. Then enter the second number when prompted.")
    print("4. The result will be displayed on the screen.")
    print("5. Check evenOdd")
    print("6. Find Percentage")
    print()
    print("You can perform as many calculations as you want.")
    print("Only numbers are accepted as input (e.g. 5, -3, 2.5).")
    print("Type 'q' to quit the calculator.")
    print("=" * 40)

def take_input():
      input1 = input("Enter input 1 :")
      input2 = input("Enter input 2 :")
      return input1, input2


show_instructions()
print()
while(True):
    operation = int(input("Enter your operation (1-6) or 'q' to quit: "))
    if operation == 'q': 
         break
    match operation:
        case 1:
            input1, input2 = take_input()
            result = float(input1) + float(input2)
            print(f"Result: {result}")
        case 2:
            input1, input2 = take_input()
            result = float(input1) - float(input2)
            print(f"Result: {result}")
        case 3:
            input1, input2 = take_input()
            result = float(input1) * float(input2)
            print(f"Result: {result}")
        case 4:
            input1, input2 = take_input()
            if float(input2) == 0:
                print("Error: Division by zero is not allowed.")
            else:
                result = float(input1) / float(input2)
                print(f"Result: {result}")
        case 5:
            input1 = input("Enter a number to check if it's even or odd: ")
            if float(input1) % 2 == 0:
                print(f"{input1} is even.")
            else:
                print(f"{input1} is odd.")
        case 6:
            input1 = input("Enter the total value: ")
            input2 = input("Enter the percentage value: ")
            result = (float(input2) / 100) * float(input1)
            print(f"{input2}% of {input1} is {result}.")
