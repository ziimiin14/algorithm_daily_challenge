class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        arr = [None] * (target+1)
        
        arr[0] = [[]]
        
        
        for x in candidates:
            for i in range(target+1):
                if arr[i] != None:
                    if i+x <= target:
                        if arr[i+x] == None:
                            arr[i+x] =[]
                        for y in arr[i]:
                            arr[i+x].append(y+[x])
        return arr[target]
                    
                        
        
        
