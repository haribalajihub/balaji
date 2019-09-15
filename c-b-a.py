n=input()
x=n[::-1]

print("-".join([x[i:i+1] for i in range(0, len(x), 1)]))
