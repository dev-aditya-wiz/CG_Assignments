#-------------------------------------------------#
#------------Q67. Cab Fare Calculator-------------#
#-------------------------------------------------#
distance = float(input("Enter distance: "))
ride_type = input("Enter ride type: ")

match ride_type:
    case "normal":
        rate = 15
    case "premium":
        rate = 25
    case _:
        print("Invalid Ride Type")
        rate = 0

fare = distance * rate

if distance > 20:
    fare = fare + (fare * 10 / 100)

if rate != 0:
    print(f"Fare: {fare:.2f}")