def maxSubArraySum(a):
	max_so_far = 0
	max_end_here = 0

	for  i in range(len(a)):
		max_end_here = max_end_here + a[i]

		if max_end_here < 0:
			max_end_here = 0

		elif (max_so_far < max_end_here):
			max_so_far = max_end_here

	return max_so_far



a = input().split()
a = list(map(int,a))

subarr_max = maxSubArraySum(a)

print(subarr_max)
