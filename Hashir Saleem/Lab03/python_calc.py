end = 'n'

def sum(a,b):
    result = a+b
    return result
    
def sub(a,b):
    result = a-b
    return result
    
def mul(a,b):
    result = a*b
    return result
    
def div(a,b):
    result = a/b
    return result
    
def parity(a):
    if a%2 == 0:
        result = "even"
    else:
        result = "odd"
    
    return result   

def percent(a,b):
    result = (a/b)*100
    return result

while end == 'n':
    operation = input("""Enter the operation you want to perform
                      '+' for addition
                      '-' for subtraction
                      '*' for multiplication
                      '/' for division
                      'e' to check for even or odd
                      '%' to calculate percentage
                      ->""")

    if operation == 'e':
        a = int(input("Enter the number: "))
    else:
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))

    if operation == '+':
        print("The result of", a, "+", b, "is", sum(a,b))

    elif operation == '-':
        print("The result of", a, "-", b,"is", sub(a,b))

    elif operation == '*':
        print("The result of", a, "*", b,"is", mul(a,b))

    elif operation == '/':
        if b == 0:
            print("Can not divide a number by 0")

        else:
            print("The result of", a, "/", b,"is", div(a,b))

    elif operation == 'e':
        print("The number", a, "is", parity(a))

    elif operation == '%':
        if b == 0:
            print("Can not calculate percentage when second number is zero")

        else:
            print(a, "is", percent(a,b), "% of", b)

    else:
        print("The operation you input is not correct")
    
    end = input("""\nDo you want to end the program?
                'y' for yes
                'n' for no
                ->""")
