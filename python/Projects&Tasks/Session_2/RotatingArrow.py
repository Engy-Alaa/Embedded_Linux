'''Python code that print 
	Animating Arrow pattern
'''
import os 
import time

def PrintUpArrow():
	#up Arrow
	# Print the top of the arrow
	for i in range(1, 4):
		print(" "*6+"  "*(4-i) + "* "*(2*i-1))
	for i in range(1, 5):
		# Print the middle line of the arrow
		print(" "*6+"  "*(4-1) + "* ")

def PrintRightArrow():	
	n=6
	m = round(((n-1)/2))+1
	
	print("\n"*3)
	for i in range (1,n):
		# Print first half of the arrow
		if(i<m):
			print(" " * 12+"  "*((n-1)-1)+"* "*i)
		# Print the middle line of the arrow	
		elif(i == m):
			print(" " * 12+"* "*((n-1)-1)+"* "*i)
		# Print second half of the arrow		
		elif(i > m):
			print(" " * 12+"  "*((n-1)-1)+"* "*((n-1)-i+1))		

def PrintDownArrow():
	print("\n"*5)	
	#down Arrow
	for i in range(1, 5):
		print(" "*6+"  "*(4-1) + "* ")
	# Print the bottom  of the arrow
	for i in range(4-2, -1, -1):
	    print(" "*6+"  "*(4-i-1) + "* "*(2*i+1))
	    
	    
def PrintLeftArrow():	
	n=6
	m = round(((n-1)/2))+1	
	print("\n"*3)	
	for i in range (1,n):
		# Print first half of the arrow
		if(i< m):
			if(i>1):
				print(" "*(m-i+1)+"* "*i)
			else:
				print(" "*(m-i+2)+"* "*i)
		# Print the middle line of the arrow		
		elif(i == m):
			print("* "*i +"* "*((n-1)-1))	
		# Print second half of the arrow	
		elif(i > m):
			if(((n-1)-i+1) > 1):
				print(" "*(m-((n-1)-i))+"* "*((n-1)-i+1))
			else:
				print(" "*(m-((n-1)-i)+1)+"* "*((n-1)-i+1))		


while True:			
			
	PrintUpArrow()		
	time.sleep(1)
	os.system('cls')

	PrintRightArrow()		
	time.sleep(1)
	os.system('cls')	
	
	PrintDownArrow()    
	time.sleep(1)
	os.system('cls')  

	PrintLeftArrow()
	time.sleep(1)
	os.system('cls')

