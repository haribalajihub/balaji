n,k=input().split()
if(n=="R" and k=="P"):
  print("P")
elif(n=="R" and k=="S"):
  print("R")
elif(n=="S" and k=="P"):
  print("S")
elif(n=="S" and k=="R"):
    print("R")
elif(n=="P" and k=="R"):
    print("P")
elif(n=="P" and k=="S"):
    print("S")
elif(n=="S" and k=="S"):
    print("D")
elif(n=="p" and k=="P"):
    print("D")
elif(n=="R" and k=="R"):
    print("D")
