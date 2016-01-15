def mean(vals):
	"""Calculate the arithmetic mean of a list of numbers in vals"""
	assert type(vals) is list, 'wrnong input format'
	
	#new_list = []					Solution 1 for test 4
	#for i in vals:					Solution 1 for test 4
	#	new_list.append(float(i))	Solution 1 for test 4
	
	vals=[float(x) for x in vals]	#Solution 2 for test 4
	
	total = sum(vals)
	length = len(vals)
	
	if length == 0:
		return 0.0
	else:
		return total/length


		
		
		
#print(mean([2,4]))

#print(mean("hello"))