def countSum(arr,targetSum):
    count = [0] * (targetSum+1)
    count[0] = 1

    for i in range(len(arr)):
        for j in range(arr[i],targetSum+1):
            count[j] += count[j-arr[i]]
        print(count)
    return count[-1]
            





arr = [2,4]
n = 10

print(countSum(arr,n))