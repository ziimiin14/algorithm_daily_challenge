class Solution:
    def lengthOfLongestSubstring(self, s):
        total_length = 0
        length = 0
        temp = ''
        for x in s:
            if x not in temp:
                temp += x
                length += 1
                
            else: 
                cut = temp.index(x)
                temp = temp[cut+1:] + x
                length -= cut
            
            if length > total_length:
                total_length = length
        
        return total_length
                
            
        
