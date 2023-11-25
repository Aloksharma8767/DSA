def subsetsUtil(A, subset, index):
	print(subset)
	for i in range(index, len(A)):
		subset.append(A[i])
		subsetsUtil(A, subset, i + 1)
		subset.pop(-1)
	return
subset = []
index = 0
a=[2,3,-2,4]
subsetsUtil(a,subset,index)
