'''
Created on Mar 15, 2015
@author:	Kelvin Rodriguez
'''

def numToBaseB_helper(N, B):
	'''helper that returns the base representation of decimal N in base B
	precondition: N is always a non-negative integer (N >=0)
	and base B is between 2 and 10 inclusive (2 <= B <= 10)'''
	if N == 0 : return ''
	return numToBaseB_helper(N / B, B) + str(N % B)

def numToBaseB(N, B):
	'''returns the base representation of decimal N in base B
	precondition: N is always a non-negative integer (N >= 0)
	and base B is between 2 and 10 inclusive (2 <= B <= 10)'''
	if N == 0 : return '0'
	return numToBaseB_helper(N, B)

def baseBToNum(S, B):
	'''returns the number representation of string S in base B
	precondition: empty string input returns 0'''
	if S == '' : return 0
	return int(S[-1]) + B * baseBToNum(S[:-1], B)

def baseToBase(B1, B2, SinB1):
	'''returns a string representing the string SinB1 in base B2'''
	return numToBaseB(baseBToNum(SinB1, B1), B2)

def add(S, T):
	'''returns the sum of input binary strings S and T in binary'''
	return numToBaseB(baseBToNum(S, 2) + baseBToNum(T, 2), 2)

# Each row has (x, y, carry-in) : (sum, carry-out)
FullAdder = { 
('0','0','0') : ('0','0'),
('0','0','1') : ('1','0'),
('0','1','0') : ('1','0'),
('0','1','1') : ('0','1'),
('1','0','0') : ('1','0'),
('1','0','1') : ('0','1'),
('1','1','0') : ('0','1'),
('1','1','1') : ('1','1') }

def addBhelper(S, T, cOut):
	'''helper function for the function addB() returns the sum of input 
	binary strings S and T as a new string in binary. The computation is 
	all done in binary i.e. no base conversion'''
	if S == '' and cOut == '1' : return '1'
	elif S == '' and cOut == '0' : return ''
	sumBit, carryBit = FullAdder[(S[-1], T[-1], cOut)]
	return addBhelper(S[:-1], T[:-1], carryBit) + sumBit

def addB(S, T):
	'''returns the sum of input binary strings S and T as a new string in 
	binary. The computation is all done in binary i.e. no base conversion'''
	if len(S) > len(T) : T = (len(S) - len(T)) * '0' + T
	else : 
		S = (len(T) - len(S)) * '0' + S
	return addBhelper(S, T, '0')

# END