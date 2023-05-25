import string
import time
import os

#Users Names List 
users = ['gvanca', 'dato', 'natia']
#Tupple That Stores Users Passwords
pswds = (1234, 5678, 9101)
#List For The Users Balance 
balances = [1000, 20000, 30000]
#Counter To Password Tries
count = 0
print("------------------------------------------------------------")
print("|                 Welcome to ATM SYSTEM                    |")
print("------------------------------------------------------------\n")



while True:
	
	user = input('ENTER USER NAME: ')
	user = user.lower()
	
	
	#Loop To Iterate Through Exist Users  
	for n in range(len(users)):
		''''If User Exist Take Password 
			And Check If It is Correct 
			Then Let The User Choose 
			From ATM Menu The Opertation
			That He Wants  
		'''
		#if User Exist In The Bank System 
		if user == users[n]:
			print('----------------')
			print('Welcome '+ user.capitalize())
			print('----------------')
			
			#Loop To Check The Password And Give The User Only 3 Tries 
			while count < 3:
				pswd = int(input("PLEASE ENTER YOUR 4 DIGIT PASSWORD: "))
				if pswd == pswds[n]:
					break
				else:
					count += 1
					print('-----------')
					print('INVALID PASSWORD')
					print('-----------')
			#In Case Of A Unvalid Pass. Exit		
			if count == 3:
				print('-----------------------------------')
				print('   3 UNSUCCESFUL PASSWORD TRIES    ')
				print('!!!!!YOUR CARD HAS BEEN LOCKED!!!!!')
				print('-----------------------------------')
				exit()
			#In Case Of A Valid Pass. Choose From Menu, or Exit	
			while True:
				os.system('cls')
				print('----------ATM SYSTEM-----------')
				print('-------------------------------')
				choice = int(input('SELECT FROM FOLLOWING OPTIONS: \n1-Your Current Balance \n2-Withdraw \n3-Deposit  \n4-Quit \nEnter The Number Of Your Choice: '))
				print('-------------------------------')
				
				#Choice 1 View Current Balance 
				if choice == 1:
					print('---------------------------------------------')
					print(user.capitalize(), 'YOU HAVE ', balances[n],'EGP ON YOUR ACCOUNT.')
					print('---------------------------------------------')
				#Choice 2 Withdraw From Balance 
				elif choice == 2:
					choice = int(input('SELECT FROM FOLLOWING OPTIONS: \n1-250\t\t4-2000 \n2-500\t\t5-2500 \n3-1000\t\t6-3000  \n7-Other \nEnter The Number Of Your Choice: '))
					if choice == 1:
						withdraw = 250
					elif choice == 2:
						withdraw = 500
					elif choice == 3:
						withdraw = 1000
					elif choice == 4:
						withdraw = 2000
					elif choice == 5:
						withdraw = 2500
					elif choice == 6:
						withdraw = 3000																								
					elif choice == 7:
						withdraw = int(input('ENTER AMOUNT YOU WOULD LIKE TO WITHDRAW: '))					
						while withdraw%10 != 0:
							print('------------------------------------------------------')
							print('AMOUNT YOU WANT TO WITHDRAW MUST TO MATCH 10 EGP')
							print('------------------------------------------------------')
							withdraw = int(input('ENTER AMOUNT YOU WOULD LIKE TO WITHDRAW: '))			
							
					if withdraw > balances[n]:
						print('-----------------------------')
						print('YOUR BALANCE IS NOT ENOUGH')
						print('-----------------------------')
					else:
						balances[n] = balances[n] - withdraw
						print('-----------------------------------')
						print('YOUR NEW BALANCE IS: ', balances[n], 'EGP')
						print('-----------------------------------')
				
				#Choice 3 Deposit To Balance 
				elif choice == 3:
					deposit = int(input('ENTER AMOUNT YOU WOULD LIKE TO DEPOSIT: '))					
					while deposit%10 != 0:
						print('------------------------------------------------------')
						print('AMOUNT YOU WANT TO WITHDRAW MUST TO MATCH 10 EGP')
						print('------------------------------------------------------')
						deposit = int(input('ENTER AMOUNT YOU WOULD LIKE TO DEPOSIT: '))
					else:
						balances[n] = balances[n] + deposit
						print('----------------------------------------')
						print('YOUR NEW BALANCE IS: ', balances[n], 'EGP')
						print('----------------------------------------')
				
				#Choice 4 Exit From System 
				elif choice == 4:
					exit()
				
				else:
					print('------------------')
					print('CHOICE NOT VALID')
					print('------------------')
				#Wait 5 Seconds And Clear Cmd After Each Operation
				time.sleep(5)	
			
			#If User Exist Write Flag To 1 	
			flag =1
			
	#Check If The Flag Is Zero So User Doesn't Exist		
	if flag == 0:
			print('----------------')
			print('INVALID USERNAME')
			print('----------------')
