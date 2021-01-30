class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """

        if len(s) < 1:
            return -1
        
        dict1={}        
        for key in s:
            dict1[key]=dict1.get(key,0)+1
            
        for k in s:
            if dict1[k]==1:
                return s.index(k)
        return -1
