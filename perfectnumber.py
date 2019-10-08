n=int(input())
a=list(map(int,input().strip().split()))[:n]
sum1 = 0
l=[]
lk=[]
for j in a:
    for i in range(1, j):
        if(n % i == 0):
            sum1 = sum1 + i
    l.append(sum1)

for kl in l:
    if (kl == l[0]):
        k='YES'
        lk.append(k)
        l[0]=l[0]+1
    else:
        k='NO'
        lk.append(k)
        l[0]=l[0]+1
for o in lk:
    print(o)
