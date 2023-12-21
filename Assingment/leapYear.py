y = int(input("enter year "))

if y%4 == 0:
    if y%100 == 0:
        if y%400 == 0:
            print ("Leap Year")
        else:
            print('not leap year')
    else:
        print("not leap year")
else:
    print("not leap year")
