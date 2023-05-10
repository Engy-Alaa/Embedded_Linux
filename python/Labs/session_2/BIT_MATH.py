'''
BIT_MATH Function File 
'''
Reg = 0

#Set The Bit In Register
def SET_BIT(REG, BIT_NUM):
	global Reg
	REG = REG	| (1 << BIT_NUM)
	Reg = REG
	return Reg

#Clear The Bit In Register
def CLR_BIT(REG, BIT_NUM):
	global Reg
	REG = REG & (~(1 << BIT_NUM))
	Reg = REG
	return Reg	
	
#Get The Bit from Register
def GET_BIT(REG, BIT_NUM):
	global Reg
	REG = (REG>> BIT_NUM) & 0x01
	Reg = REG
	return Reg	
	
#Toggle The Bit In Register
def TOG_BIT(REG, BIT_NUM):
	global Reg
	REG = REG ^(1 << BIT_NUM)
	Reg = REG
	return Reg	
