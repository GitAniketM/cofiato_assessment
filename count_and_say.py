class Solution:
    def countAndSay(self, n: int) -> str:
        '''
        if n = 1, then ans = "1"
        if n = 2, then ans = "11" i.e, count+value
        if n = 3, then ans = "21" i.e, count = 2 + value = 1
        if n = 4, then ans = "1211" i.e, count(2) = 1 and value = 2 thus, 12 then count(1) = 1 and 
        value = 1 thus, 11 summing both, 1211
        '''
        if n == 1: return "1"
        if n == 2: return "11"
        
        # for greater than 2 let, 
        inString = "11"   # answer till for n=2
        
        for i in range(3, n+1):
            inString += '#'
            curr = ""
            count = 1
            
            for j in range(1, len(inString)):
                if inString[j] == inString[j-1]:
                    count += 1
                else:
                    # means they are different, so then for the first elements
                    # we do count and say, so add count first then value
                    curr += str(count)
                    curr += inString[j-1]
                    count = 1
            
            inString = curr
        
        return inString