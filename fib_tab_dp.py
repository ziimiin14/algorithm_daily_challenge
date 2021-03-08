def fib_tab(target):
    arr = [0,1]

    for i in range(2,target+1):
        arr.append(arr[i-2]+arr[i-1])
    
    return arr[target]

print(fib_tab(6))

print(fib_tab(7))

print(fib_tab(8))

print(fib_tab(50))
