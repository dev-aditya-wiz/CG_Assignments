#-------------------------------------------------------------#
#------------Q53. Traffic Signal Using match-case-------------#
#-------------------------------------------------------------#
color = input("Enter signal color: ")

match color:
    case "red":
        print("Stop")
    case "yellow":
        print("Wait")
    case "green":
        print("Go")
    case _:
        print("Invalid Signal")