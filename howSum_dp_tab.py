def howSum_tab(targetSum,numbers):
    table = [None]*(targetSum+1)

    table[0] = []

    for i in range(targetSum+1):
        if table[i] != None:
            for number in numbers:
                if i+number<=targetSum:
                     table[i+number] = table[i] + [number]
    print(table)
    return table[targetSum]

def howSum_tab1(targetSum,numbers):
    table = [None]*(targetSum+1)

    table[0] = []

    for i in range(len(numbers)):
        for j in range(numbers[i],targetSum+1):
            if table[j-numbers[i]] != None:
                table[j] = table[j-numbers[i]] + [numbers[i]]
    print(table)
    return table[targetSum]



print(howSum_tab(10,[1,3]))
print(howSum_tab1(10,[1,3]))

