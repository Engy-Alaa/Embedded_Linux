'''Python code That print 
    1-Bit Wise
    2-Math Opperations
    3-relation Between two Variables
'''
#Take Two Num From User
MyNum1 = int(input("Please enter Num 1: "))
MyNum2 = int(input("Please enter Num 2: "))

#Bit Wise opperators
print(str(MyNum1) +"|"+str(MyNum2)+"="+str(bin(MyNum1 | MyNum2)))
print(str(MyNum1) +"&"+str(MyNum2)+"="+str(bin(MyNum1 & MyNum2)))
print(str(MyNum1) +"^"+str(MyNum2)+"="+str(bin(MyNum1 ^ MyNum2)))
print("~"+str(MyNum2)+"="+str(~MyNum1))

#Arithmatic opperators
print(str(MyNum1) +"+"+str(MyNum2)+"="+str((MyNum1 + MyNum2)))
print(str(MyNum1) +"-"+str(MyNum2)+"="+str((MyNum1 - MyNum2)))
print(str(MyNum1) +"*"+str(MyNum2)+"="+str((MyNum1 * MyNum2)))
print(str(MyNum1) +"/"+str(MyNum2)+"="+str((MyNum1 / MyNum2)))

#relation Between two Variables
print(str(MyNum1) +">"+str(MyNum2)+"="+str(MyNum1 > MyNum2))
print(str(MyNum1) +"=="+str(MyNum2)+"="+str(MyNum1 == MyNum2))
print(str(MyNum1) +">="+str(MyNum2)+"="+str(MyNum1 >= MyNum2))

