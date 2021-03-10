def canSum_tab(targetSum,numbers):
    arr = [bool(0)]*(targetSum+1)

    arr[0] = True

    for i in range(len(arr)):
        if arr[i] == True:
            for x in numbers:
                if x+i <= targetSum:
                    arr[x+i]  = True
    return arr[targetSum]



print(canSum_tab(7,[5,3,4]))
        