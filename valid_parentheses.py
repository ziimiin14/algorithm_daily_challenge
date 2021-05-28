class Solution:
    def isValid(self, s: str) -> bool:
        record = []
        for x in s:
            if x is '(' or x is '[' or x is '{':
                record.append(x)
                
            else:
                if len(record) == 0:
                    return False
                else:
                    
                    pop_last = record.pop()
                    if pop_last is '(':
                        if x is not ')':
                            return False

                    if pop_last is '{':
                        if x is not '}':
                            return False

                    if pop_last is '[':
                        if x is not ']':
                            return False
                    
        if len(record) != 0:
            return False
        
        return True
                    
                
            
