n=int(input())
a=list(map(int,input().strip().split()))[:n]
sum=0
num=0
for i in range(len(a)-1):
    sum = a[i] + a[i + 1] 
    num=sum+num

print(num)
