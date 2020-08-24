lst= [4,5,6,1,2,8,23,54,12,32,4,1,9]

def sort1(arr):
	for i in range(len(arr)-1,0,-1):
		
		for j in range(i):
			if arr[j]>arr[j+1]:
				temp=arr[j+1]
				arr[j+1]=arr[j]
				arr[j]=temp
	print(arr)
sort1(lst)					
			
				
