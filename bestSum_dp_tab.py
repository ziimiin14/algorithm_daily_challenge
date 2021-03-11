def bestSum_tab(targetSum,numbers):
    # table = [None]*(targetSum+1)
    table = [None]*(targetSum+1)
    
    table[0] = []

    for i in range(targetSum+1):
        if table[i] != None:
            for number in numbers:
                if i+number<=targetSum:
                    temp = table[i] + [number]
                    if table[i+number] == None:
                        table[i+number] = table[i] + [number]
                    else:
                        if len(temp) < len(table[i+number]):
                            table[i+number] = temp

    return table[targetSum]


print(bestSum_tab(8,[1,3,6,2,8]))

