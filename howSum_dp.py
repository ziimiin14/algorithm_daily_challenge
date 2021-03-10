def howSum(targetSum,numbers,memo):
    if targetSum in memo:
        return memo[targetSum]
    if targetSum == 0:
        return []

    if targetSum < 0 :
        return

    
    for number in numbers:
        remainder = targetSum-number
        # print(number)
        remainderRes = howSum(remainder,numbers,memo)
        # print(remainderRes)

        if  remainderRes !=  None:
            temp = remainderRes.copy()
            temp.append(number)
            # print(remainderRes)
            memo[targetSum] = temp
            # print(targetSum,temp,memo)
            return memo[targetSum]

    memo[targetSum] = None
        
    return None



b = {} 
print(howSum(10,[2,4],b))


             