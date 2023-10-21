def calculate(first_val, second_val, action):
    if action == 1:
        return "Addition of {} and {} is: ".format(first_val, second_val), first_val+second_val
    elif action == 2:
        return "Substraction of {} and {} is: ".format(first_val, second_val), first_val-second_val
    elif action == 3:
        return "Multiplication of {} and {} is: ".format(first_val, second_val), first_val*second_val
    elif action == 4:
        return "Division of {} and {} is: ".format(first_val, second_val), first_val/second_val


def advance_calc(first_val, action):
    if action == 5:
        return "Square of {} is".format(first_val), first_val**2
    elif action == 6:
        return "Square root of {} is: ".format(first_val), first_val**0.5
    elif action == 7:
        return "fahrenheit {} to celsius is: ".format(first_val), ((first_val-32)*(5.0/9.0))
    elif action == 8:
        return "celsius {} to fahrenheit is: ".format(first_val), ((9.0/5.0) * first_val) + 32


Ops = {1: 'Add', 2: 'Subtract', 3: 'Multiply', 4: 'Divide', 5: 'Square', 6: 'Square root', 7: 'fahrenheit to celsius',
       8: 'celsius to fahrenheit'}
operation = 0
while operation == 0:
    try:
        operation = input("Choose your operation in numeric form:\n 1: Add \n 2: Subtract\n 3: Multiply\n 4: Divide\n"
                          " 5: Square\n 6: Square root : ")
        if int(operation) not in Ops.keys():
            print('\n', '*' * 8, "Entered operation {} is not specified, please try again from given operations".
                  format(operation), '*' * 8)
            operation = 0
    except NameError:
        print('\n', '*' * 8, "Please choose numeric value of desired operation and try again", '*' * 8)

print('+' * 5, "You have selected the {} Operation".format(Ops[int(operation)]), '+' * 5)
if int(operation) in range(1, 5):
    a = input('Enter first value: ')
    b = input('Enter second value: ')
    print(calculate(first_val=int(a), second_val=int(b), action=int(operation)))
else:
    a = input('Enter your value: ')
    print(advance_calc(first_val=int(a), action=int(operation)))
