#---------------------------------------------------------#
#------------Q52. Calculator Using match-case-------------#
#---------------------------------------------------------#
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
operator = input("Enter operator: ")

match operator:
    case "+":
        print(a + b)
    case "-":
        print(a - b)
    case "*":
        print(a * b)
    case "/":
        print(a / b)
    case _:
        print("Invalid Operator")