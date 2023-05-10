'''Python Code Asks User To Choose Between Functions 
And Learn It's Function By Showing Example 
'''
	
Value = int(input("To Understand isupper Function Press \'1\'\n To Understand lower Function Press \'2\' \n--> "))
		
if Value == 1:
	print("isupper() Function : Returns True if all characters in \nthe string are upper case \nExample:")
	print(''' txt = "THIS IS NOW!"
 x = txt.isupper()
 print(x)\n''')
	
	txt = "THIS IS NOW!"
	x = txt.isupper()
	print("Output: "+str(x))
	

elif Value == 2:
	print("lower() Function : Converts a string into lower case \nExample:")
	print('''txt = "Hello my FRIENDS"
 x = txt.lower()
 print(x)\n''')
	txt = "Hello my FRIENDS"
	x = txt.lower()
	print("Output: "+str(x)) 
