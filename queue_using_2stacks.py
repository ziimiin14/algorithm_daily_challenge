# Enter your code here. Read input from STDIN. Print output to STDOUT



def solve(arr,temp):
    if len(temp) == 2:
        arr.append(temp[1])
    
    else:
        if temp[0] == 2:
            arr.pop(0)
        else:
            if arr:
                print(arr[0])
                
    return arr

if __name__ == "__main__":
    n = int(input())
    arr = []


    for i in range(n):
        g = input()
        temp = list(map(int,g.split()))
        arr  = solve(arr,temp)

    

