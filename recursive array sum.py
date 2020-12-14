
# Recursively sums the elements from end to start
def sum(array,len):

	if len == 1: #base case
		return array[0]
	else:
		new_len = len -1
		return array[len-1] + sum(array,new_len)



# Recursively sums the elements from start to end
def sum2(array,index):

	if(index == len(array) -1): #base case
		return array[index]
	else:
		new_index = index + 1
		return array[index] + sum2(array , new_index)

array = [33,4,5,6]

print(sum(array,4))
print(sum2(array,0))