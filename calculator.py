import calculator;
Num1=int(input("enter the Num1:"))
Num2=int(input("enter the num2:"))
Operation=input("add/sub/mul/div:")
if(Operation=="add"):
    print(Num1+Num2)
elif(Operation=="sub"):
    print(Num1-Num2)
elif(Operation=="mul"):
    print(Num1*Num2) 
elif(Operation=="div"):
    print(Num1/Num2) 
else:
    print("Invalid Operation")              