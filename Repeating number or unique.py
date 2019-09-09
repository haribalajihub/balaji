def printRepeating(arr, size): 

    for i in range (0, size): 

        for j in range (i + 1, size): 

            if arr[i] == arr[j]: 

                print(arr[i], end = ' ') 
            else:
                print("unique")
n=int(input())
arr = list(map(int,input().strip().split()))[:n] 


arr_size = len(arr) 
printRepeating(arr, arr_size)
