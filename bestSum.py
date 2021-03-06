def bestSum(targetSum,numbers,memo):
    if targetSum in memo:
        return memo[targetSum]

    if targetSum == 0:
        return []

    if targetSum < 0 :
        return

    shortestCombination = None

    for num in numbers:
        remainder = targetSum - num
        remainderRes =bestSum(remainder,numbers,memo)

        if remainderRes != None:
            temp = remainderRes.copy()
            temp.append(num)
            # for x in remainderRes:
            #     temp.append(x)

            # temp.append(num)
            # print(memo)
            
            if (shortestCombination == None) or (len(temp) < len(shortestCombination)):
                shortestCombination = temp
                
            
           
    memo[targetSum] = shortestCombination

    
    return shortestCombination
            
b  ={}
print(bestSum(10,[2,4],b))
c = {}
# print(bestSum(100,[1,2,5,25],c))
d = {}
# print(bestSum(301,[7,14],d))
