n,k =input().split()
n=int(n)
k=int(k)

Oddtotal = 0

for number in range(n, k+1):
    if(number % 2 != 0):
        Oddtotal = Oddtotal + number

print(Oddtotal) 
