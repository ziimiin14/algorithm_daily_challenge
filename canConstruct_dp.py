def canConstruct(target,wordBank,memo):
    if target in memo:
        return memo[target]

    if target == '':
        return True

    for x in wordBank:

        if target.find(x) ==0:
            newStr = target[len(x):]
            check = canConstruct(newStr,wordBank,memo) 
            if check:
                memo[target] = True
                return True


    memo[target] = False

    return False





# test case

a = 'abcdefghi'
b = ['ab','abc','abcd','cd','ef','gh','i','efgh','def','ghi']
c = {}


d = 'eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef'
e = ['e','eee','eeeeeee','ee']
f = {}
print(canConstruct(a,b,c))
print(canConstruct(d,e,f))