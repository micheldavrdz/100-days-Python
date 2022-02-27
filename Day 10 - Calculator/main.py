def main():

    from calc_logo import logo
    import os

    # add, subtract, multiply, divide functions
    def add(number_1, number_2):
        return number_1 + number_2

    def subtract(number_1, number_2):
        return number_1 - number_2

    def multiply(number_1, number_2):
        return number_1 * number_2

    def divide(number_1, number_2):
        return number_1 / number_2

    # Calculate function (takes in user's numbers and operation selected)
    def calculate(number_1, number_2, operator):
        if operator == '+':
            return add(number_1, number_2)
        elif operator == '-':
            return subtract(number_1, number_2)
        elif operator == '*':
            return multiply(number_1, number_2)
        elif operator == '/':
            return divide(number_1, number_2)
        else:
            return 'Invalid operator'

    # Operations dictionary to show user the available operations (could be done with a list, but this is more readable)
    operations = {
        '+': add,
        '-': subtract,
        '*': multiply,
        '/': divide
    }

    def calculator():

        finish_calculation = False
        
        print(logo)

        user_num1 = float(input('\nPlease enter your first number: '))

        # Keep the program running until the user is done
        while not finish_calculation:
            # Simple empty line to make the output look nicer
            print('')
            
            # Show the user the available operations
            for operation in operations:
                print(operation)

            operation_symbol = input('\nWhat operation would you like to perform?: ')

            user_num2 = float(input('\nPlease enter your second number: '))
            
            # Call the calculate function with the user's input parameters
            final_result = calculate(user_num1, user_num2, operation_symbol)
            
            # Print the calculation result
            print(f'\n{user_num1} {operation_symbol} {user_num2} is: {final_result}')
            
            # Change user_num1 to the final result so the user can continue to calculate if they want to
            user_num1 = final_result
            
            desicion = input(f'\nWould you like to : \n1. Continue calculating using the last answer ({final_result})? (Type 1) \n2. Start a fresh calculation (Type 2) \n3. Exit the calculator (Type any other number or letter) \n\nPlease enter your answer: ')
            
            # Don't do anything and keep calculating
            if desicion == '1':
                pass
            # Clear the screen and call the calculator function again
            elif desicion == '2':
                finish_calculation = True
                
                # Clear the screen for better readability, clear only works on macOS and Linux (posix) while cls only works on Windows (nt)
                if(os.name == 'posix'):
                    os.system('clear')
                else:
                    os.system('cls')
                    
                calculator()
            # Exit the program
            else:
                finish_calculation = True
                print('\nThank you for using the calculator!')

    # Start the calculator                
    calculator()

if __name__ == '__main__':
    main()