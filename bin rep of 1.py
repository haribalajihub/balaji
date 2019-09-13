import math 
  
def BitPos(n): 
     return math.log2(n&-n)+1  
n = int(input())
print(int(BitPos(n)))
