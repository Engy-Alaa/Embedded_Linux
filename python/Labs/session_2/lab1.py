'''Python code Recive Five Values From User
	Ask User To Request Number
    Then Print Exist if It Found
'''
#Take Two Num From User
Value1 = int(input("Please enter Value 1: "))
Value2 = int(input("Please enter Value 2: "))
Value3 = int(input("Please enter Value 3: "))
Value4 = int(input("Please enter Value 4: "))
Value5 = int(input("Please enter Value 5: "))

#Store Values In Set
MySet = {Value1, Value2, Value3, Value4, Value5}

Value = int(input("Please enter Value To Search: "))

if Value in MySet:
	
	print("Value Exist")

else:
	print("Sorry Value Does Not Exist")
