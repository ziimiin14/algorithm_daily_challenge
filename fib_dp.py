def fib_num(n,memo):
    if n in memo:
        return memo[n]
    if n<=2:
        return 1
    
    memo[n] = fib_num(n-1,memo)+fib_num(n-2,memo)
    return memo[n]

a = 120
b = {}
res = fib_num(a,b)
print(b)
print(res)