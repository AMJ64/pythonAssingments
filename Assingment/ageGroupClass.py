n = 18

match n:
    case num if n<18:
        print("Underage")
    case num if n>=18 and n<=35:
        print("18-35")
    case num if n>=36 and n<=60:
        print("36-60")
    case num if n>=61:
        print("above 60")
    case 0:
        print("lol")
    