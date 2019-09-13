import math 
y=int(input())
x=int(input())
def Log2(x): 
    return (math.log10(x) / math.log10(2)); 

def isPowerOfTwo(x): 
    return (math.ceil(Log2(x)) == math.floor(Log2(x))); 

if(isPowerOfTwo(y)): 
    print("yes"); 
else: 
    print("no"); 
