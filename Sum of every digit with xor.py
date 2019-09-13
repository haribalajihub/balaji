num = int(input())  
sum = 0    
y=0
   
Reverse = 0    
while(num > 0):    
    Reminder = num %10    
    Reverse = (Reverse *10) + Reminder    
    num = num //10    

temp=Reverse
while temp > 0:  
   digit = temp % 10  
   sum += digit**y
   y=y+1
   temp //= 10
print(sum)
