'''open file and edit in it
'''
#Take Data From User
name = input("Please enter your Name: ")
age = input("Please enter Age: ")


#Open File Store Data To File
myfile = open("file.txt","a+")
myfile.write("Name: ")
myfile.write(name+"\n")
myfile.write("Age: ")
myfile.write(age+"\n")
#read Data From File
myfile = open("file.txt","r")
print(myfile.read())

myfile.close()

