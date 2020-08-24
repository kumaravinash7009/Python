lst= [4,5,6,1,2,8,23,54,12,32,4,1,9]

def bubsort(list):
	for i in range(len(list)-1):
		minpos=i
		for j in range(i,len(list)):		
			if list[j]<list[minpos]:
				minpos=j
		list[i],list[minpos]=list[minpos],list[i]	
	print(list)
	
bubsort(lst)				
			
		
