#control flow statements
#condition statements
marks = int(input("enter marks "))
if(marks>80 and marks<=100):
    print("A grade")
elif(marks>65 and marks<=80):
    print("B grade")
elif(marks>45 and marks<=65):
    print("C grade")
elif(marks>33 and marks<=45):
    print('D grade')
elif(marks>0 and marks<=33):
    print("Failed successfully")
else:
    print('Invalid Number')
    

