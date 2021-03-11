def allSumConstruct_tab(targetSum,numbers):
    # table = [None]*(targetSum+1)
    table = [None]*(targetSum+1)
    
    table[0] = []

    for i in range(targetSum+1):
        if table[i] != None:
            for number in numbers:
                if i+number<=targetSum:
                    temp = table[i] + [number]
                    if table[i+number] == None:
                        table[i+number] = []
                    if i == 0:
                        temp = table[i] + [number]
                        table[i+number].append(temp)
                    for j in range(len(table[i])):
                        temp = table[i][j] + [number]
                        table[i+number].append(temp)
                    
                    #     table[i+number].append([temp])
                    # else:
                    #     table[i+number].append([temp])

    return table[targetSum]


print(allSumConstruct_tab(8,[4,2]))

