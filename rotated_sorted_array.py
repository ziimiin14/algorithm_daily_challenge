class Solution:
    def search(self, nums: List[int], target: int) -> int:
        length = len(nums)
        pivot = length - nums.index(min(nums))
        
        low = -pivot
        high = length-1-pivot
        final = None
        
        while (low<= high):
            middle = (high+low)//2
            print(middle)
            
            if nums[middle] == target:
                final = middle
                break
    
            elif nums[middle] < target:
                low = middle +1
            else:
                high = middle -1
        
        if final == None:
            return -1
        if final < 0:
            final += length
            
        return final
            
        
        
        
