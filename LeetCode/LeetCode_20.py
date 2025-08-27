class Solution:
    # O(1)
    def isValid(self, s: str) -> bool:
        stack = []
        for symbol in s:                    
            if symbol in '([{':             
                stack.append(symbol)        
            else:                           
                if not stack:               
                    return False
                top = stack.pop()           
                if (symbol == ')' and top != '(') or \
                   (symbol == ']' and top != '[') or \
                   (symbol == '}' and top != '{'):
                    return False            

        return not stack    
