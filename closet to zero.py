def minAbsSumPair(arr,arr_size): 
	inv_count = 0


	if arr_size < 2: 
		print("Invalid") 
		return

	min_l = 0
	min_r = 1
	min_sum = arr[0] + arr[1] 
	for l in range (0, arr_size - 1): 
		for r in range (l + 1, arr_size): 
			sum = arr[l] + arr[r]				 
			if abs(min_sum) > abs(sum):		 
				min_sum = sum
				min_l = l 
				min_r = r 

	print(arr[min_l],arr[min_r]) 

n = int(input()) 

arr = list(map(int,input().strip().split()))[:n] 

minAbsSumPair(arr, n);  
