class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)
    
'''
Used simple python function find to find the index(x)
what it does basically is, it will return the first 
occurence of existence of needle in haystack and terminate
the loop. Its apprx O(n) time complexity
'''