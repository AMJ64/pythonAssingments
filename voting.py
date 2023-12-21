nationality  = input("Enter Country Name in FULL CAPITAL ")
age  = int(input("Enter Age of Candidate "))
S = "INDIAN"
if nationality==S:
    if age>=18:
        print("eligible to vote")

    else:
        print("Not Eligible, Underage")
    
else:
    print("Not Eligible, not a citizen")