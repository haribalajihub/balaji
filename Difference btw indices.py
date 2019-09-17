n=int(input())
a=list(map(int,input().strip().split()))[:n]
x=max(a)
y=min(a)
b=a.index(x)
c=a.index(y)
print(b-c)
