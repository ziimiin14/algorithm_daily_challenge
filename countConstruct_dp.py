def countConstruct(target,wordBank,memo):
    if target in memo:

        return memo[target]

    if target == '':

        return 1

    totalCount = 0

    for x in wordBank:

        if target.find(x) ==0:
            newStr = target[len(x):]
            count = countConstruct(newStr,wordBank,memo) 
            
            totalCount += count


    memo[target] = totalCount
    # print(memo)
    
    return totalCount


a = 'abcdefghi'
b = ['ab','abc','abcd','cd','ef','gh','i','efgh','def','ghi']
c = {}


d = 'eeeeeeeeeeeeeeeeeeeeeeeeeee'
e = ['e','ee','eee']
f = {}
print(countConstruct(a,b,c))
print(countConstruct(d,e,f))