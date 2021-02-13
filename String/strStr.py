class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(haystack) < len(needle):
            return -1
        if len(needle) < 1:
            return 0
        
        c=-1
        h=0
        ln = len(needle)
        while h < len(haystack)-ln+1:  
            if haystack[h:h+ln]==needle:
                return h
            h=h+1
        return -1
