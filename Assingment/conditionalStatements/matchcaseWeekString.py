n = input("enter the string ")

match n:
    case "sun":
        print("Sunday")
    case "mon":
        print("Monday")
    case "tue":
        print("Tuesday")
    case "wed":
        print("Wednesday")
    case "thu":
        print("thursday")
    case "fri":
        print("Friday")
    case "sat":
        print("Saturday")
    case _:#this is used as match case else 
        print("Invalid Day")