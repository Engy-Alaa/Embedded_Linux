'''calc store ans to file
'''
	
def sub(x,y):
	ans = x-y
	return ans
def add(x,y):
	ans = x+y
	return ans
def div(x,y):
	ans = x/y
	return ans
def mul(x,y):
	ans = x*y
	return ans
num1 = int(input("Please enter No.1: "))
oper = input("Please enter chose opperation \'+' \'-' \'*' \'\\' \nop: ")
num2 = int(input("Please enter No.2: "))
res=0
#switch on operation
if oper =='+':
	res = add(num1,num2)
elif oper == '-':
	res = sub(num1,num2)
elif oper == '*':
	res = mul(num1,num2)
elif oper == '/':
	res = div(num1,num2)
#Open File Store Data To File
myfile = open("calc.txt","a+")
myfile.write(str(num1)+oper+str(num2)+" = "+str(res) +"\n")

#read Data From File
myfile = open("calc.txt","r")
print(myfile.read())

myfile.close()
