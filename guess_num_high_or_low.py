# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        low = 1
        high = n
        
        while low <= high:
            middle = low+(high-low)//2
            res = guess(middle)
            
            if res == 0:
                return middle
            elif res == -1:
                high = middle-1
                
            else:
                low = middle + 1
                
