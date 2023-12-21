n = input("enter query ")

match n:
    case "Processing":
        print("order in process")
    case "Shipped":
        print('order Shipped')
    case "Delivered":
        print("order Delivered")