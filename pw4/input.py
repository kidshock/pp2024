def input_positive_number(prompt):
    while True:
        try:
            number = int(input(prompt))
            if number > 0:
                return number
            print("Number must be greater than 0.")
        except ValueError:
            print("Invalid input. Please enter a number.")