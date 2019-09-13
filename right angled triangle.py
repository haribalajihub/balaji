a =int(input())
b =int(input())
c =int(input())
def checkValidity(a, b, c):
	if (a + b <= c) and (a + c <= b) and (b + c <= a) :
		return False
	else:
		return True
if checkValidity(a, b, c): 
	print("yes")
else:
	print("no")
