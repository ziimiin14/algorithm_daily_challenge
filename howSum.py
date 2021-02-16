def howSum(targetSum,numbers,memo):
    if targetSum in memo:
        return memo[targetSum]
    if targetSum == 0:
        return []

    if targetSum < 0 :
        return

    
    for number in numbers:
        remainder = targetSum-number
        remainderRes = howSum(remainder,numbers,memo)

        if  remainderRes !=  None:
            remainderRes.append(number)
            memo[targetSum] = remainderRes
            return memo[targetSum]

    memo[targetSum] = None
        
    return None



b = {} 
print(howSum(300,[7,14],b))


             