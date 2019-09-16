s = int(input())
a=list(map(int,input().strip().split()))[:s]

ran = len(a) 
sum=0
for element in range(0,ran):
    print(a[element]+sum,end=' ')
    sum=a[element]+sum

