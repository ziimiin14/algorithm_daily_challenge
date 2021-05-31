class Solution:
    def romanToInt(self, s: str) -> int:
        total = 0
        i = 0
        length = len(s)
        symbol_val = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        while i < length :
            if i < length-1 and symbol_val[s[i]] < symbol_val[s[i+1]] :
                total = total - symbol_val[s[i]] + symbol_val[s[i+1]]
                i += 2
                    
            else:
                total = total + symbol_val[s[i]]
                i += 1
        
        return total
                
        
