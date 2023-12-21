#match case
n = int(input('enter the number of week day '))
'''
if n>=1 and n<=7:
    if n==1:
        print("Monday")
    elif n==2:
        print("Tuesday")
    elif n==3:
        print('Wednesday')
    elif n==4:
        print("Thursday")
    elif n==5:
        print("Friday")
    elif n==6:
        print("Saturday")
    elif n==7:
        print("Sunday")
else:
    print("invalid number")
    '''

#matchcase  and also called as switch case

match n:
    case 1:
        print("Sunday")
    case 2:
        print("Monday")
    case 3:
        print("Tuesday")
    case 4:
        print("Wednesday")
    case 5:
        print("thursday")
    case 6:
        print("Friday")
    case 7:
        print("Saturday")
    case _:#this is used as match case else 
        print("Invalid Day")

