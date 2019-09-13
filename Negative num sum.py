n=int(input())
a=list(map(int,input().strip().split()))
y=list(filter(lambda x: (x < 0), a))
print(sum(y))
