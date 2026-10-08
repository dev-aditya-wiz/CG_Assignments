#-------------------------------------------------------#
#------------Q44. Greatest of Three Numbers-------------#
#-------------------------------------------------------#
a = int(input("Enter A: "))
b = int(input("Enter B: "))
c = int(input("Enter C: "))

if a >= b:
    if a >= c:
        if a == b and a == c:
            print("All are Equal")
        elif a == b:
            print("A and B are Equal and Greatest")
        elif a == c:
            print("A and C are Equal and Greatest")
        else:
            print("A is Greatest")
    else:
        print("C is Greatest")
else:
    if b >= c:
        if b == c:
            print("B and C are Equal and Greatest")
        else:
            print("B is Greatest")
    else:
        print("C is Greatest")