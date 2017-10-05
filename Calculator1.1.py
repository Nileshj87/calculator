def Calculate(a,b,operation):
    if operation == 1:
        return "Addtion of {} and {} is: ".format(a,b) , a+b
    elif operation == 2:
        return "Substraction of {} and {} is: ".format(a,b) , a-b
    elif operation == 3:
        return "Multiplication of {} and {} is: ".format(a,b) , a*b
    elif operation == 4:
        return "Division of {} and {} is: ".format(a,b) , a/b
def Advance_Calc(a,operation):
    if operation==5:
        return "Square of {} is".format(a) , a**2
    elif operation==6:
        return "Square root of {} is: ".format(a), a**0.5
    elif operation==7:
        return "fahrenheit {} to celsius is: ".format(a), ((a-32)*(5.0/9.0))
    elif operation==8:
        return "celsius {} to fahrenheit is: ".format(a), ((9.0/5.0) * a ) + 32


Ops = {1:'Add', 2:'Substract', 3:'Muliply', 4:'Divide', 5:'Square', 6:'Square root',7:'fahrenheit to celsius',8:'celsius to fahrenheit'}
operation = 0
while operation == 0:
    try:
        operation = input("Choose your operation in numric form:\n 1: Add \n 2: Substract\n 3: Muliply\n 4: Divide\n 5: Square\n 6: Square root : ")
        if not operation in Ops.keys():
            print '\n','*' * 8, "Entered operation {} is not specified, please try again from given oprations".format(operation), '*' * 8
            operation = 0
    except NameError:
        print '\n','*' * 8, "Please choose numric value of desired operation and try again" , '*' * 8

print '+'* 5, "You have selected the {} Operation".format(Ops[operation]),'+'* 5
if operation in range(1,5):
    a = input('Enter first value: ')
    b = input('Enter second value: ')
    print Calculate(a,b,operation)
else:
    a = input('Enter your value: ')
    print Advance_Calc(a,operation)
