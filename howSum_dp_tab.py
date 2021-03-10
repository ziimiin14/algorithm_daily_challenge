def howSum_tab(targetSum,numbers):
    table = [None]*(targetSum+1)

    table[0] = []

    for i in range(targetSum+1):
        if table[i] != None:
            for number in numbers:
                if i+number<=targetSum:
                     table[i+number] = table[i] + [number]
    # print(table)
    return table[targetSum]


print(howSum_tab(294,[7,14]))

