X=int(input())
c=str(1)

for i in range(1,X+1):
    for j in range(0,X-i):
        print(c+"",end=" ")
    print(c.strip())
