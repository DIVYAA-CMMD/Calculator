while True:
    print("\n========== CALCULATOR ==========")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Square")
    print("6. Cube")
    print("7. Percentage")
    print("8. Average")
    print("9. Unit Converter")
    print("10. Exit")
    choice = input("Enter your choice: ")

    if choice == "10":
        print("Thank you for using the calculator!")
        break
    elif choice == "9":
        print("\n========== UNIT CONVERTER ==========")
        print("1. Kilometers to Meters")
        print("2. Meters to Kilometers")
        print("3. Kilograms to Grams")
        print("4. Grams to Kilograms")
        print("5. Celsius to Fahrenheit")
        print("6. Fahrenheit to Celsius")
        converter_choice = input("Enter your choice: ")
        if converter_choice == "1":
            km = float(input("Enter distance in kilometers: "))
            print("Meters =", km * 1000)
        elif converter_choice == "2":
            meters = float(input("Enter distance in meters: "))
            print("Kilometers =", meters / 1000)
        elif converter_choice == "3":
            kg = float(input("Enter weight in kilograms: "))
            print("Grams =", kg * 1000)
            
        elif converter_choice == "4":
            grams = float(input("Enter weight in grams: "))
            print("Kilograms =", grams / 1000)
        elif converter_choice == "5":
            celsius = float(input("Enter temperature in Celsius: "))
            print("Fahrenheit =", (celsius * 9 / 5) + 32)
        elif converter_choice == "6":
            fahrenheit = float(input("Enter temperature in Fahrenheit: "))
            print("Celsius =", (fahrenheit - 32) * 5 / 9)
    
    if choice == "1":
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print("Result =", num1 + num2)
    elif choice == "2":
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print("Result =", num1 - num2)
    elif choice == "3":
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print("Result =", num1 * num2)
    elif choice == "4":
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
        if num2 == 0:
            print("Cannot divide by zero.")
        else:
            print("Result =", num1 / num2)
    elif choice == "5":
        num = float(input("Enter a number: "))
        print("Square =", num ** 2)
    elif choice == "6":
        num = float(input("Enter a number: "))
        print("Cube =", num ** 3)
    elif choice == "7":
        num = float(input("Enter the number: "))
        percent = float(input("Enter the percentage: "))
        print("Result =", (num * percent) / 100)
    elif choice == "8":
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print("Average =", (num1 + num2) / 2)