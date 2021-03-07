def allConstruct(target,wordBank,memo):
    if target in memo:
        print(memo[target])
        return memo[target]


    if target == '':
        return [[]]
    
    totalArray = []
    for word in wordBank:
        if target.find(word) == 0:
            newStr = target[len(word):]
            suffixWays = allConstruct(newStr,wordBank,memo)
            for i in range(len(suffixWays)):
                suffixWays[i].insert(0,word)
                temp = [suffixWays[i].copy()]
                totalArray += temp
                # print(target)
                # print(totalArray)


    memo[target] = totalArray
    # print(memo)

    return totalArray


# a = 'abcdefghi'
# b = ['ab','abc','abcd','cd','ef','gh','i','efgh','def','ghi']
# c = {}


d = 'abcdef'
e = ['ab','abc','cd','def','abcd','ef','c']
f = {}
# print(allConstruct(a,b,c))
print(allConstruct(d,e,f))