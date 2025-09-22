number1 = int(input( 'enter your number' ))
number2 = int (input( 'enter your number' ))

your_operation = input(""" which operation do you want to use
                       + for addition
                       - for subtraction
                       * for multiplication
                       / for division
                       enter here""")

if your_operation == "+":
    print('your answer is', number1 + number2)

elif your_operation == "-":
    print('your answer is', number1 - number2)

elif your_operation == "*":
    print('your answer is', number1 * number2)

elif your_operation == "/":
    if number2 == 0:
        print('undefined answer')
    else:
        print('your answer is', number1 / number2)
    

else:
    print('you have entered the wrong operation')
