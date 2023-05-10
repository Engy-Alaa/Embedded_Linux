'''Python code Recive Three Sensors Values From User
    Store in :
    1-Dict
    2-List
    3-Tuple
    Then Print Them
'''
#Take Two Num From User
Value1 = input("Please enter Value 1: ")
Value2 = input("Please enter Value 2: ")
Value3 = input("Please enter Value 3: ")

#Store Values In List
MyList = [Value1, Value2, Value3]

#Store Values In List
MyTuple = (Value1, Value2, Value3)

#Store Values In Dict
MyDict = { "Value1": Value1, "Value2": Value1, "Value3": Value3 }

#Print List
print(MyList)

#Print Tuple
print(MyTuple)

#Print Dict
print(MyDict)




