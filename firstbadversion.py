class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        temp=n
        if temp==1:
            return temp
          
        for i in range(m):
            if isBadVersion(i):
                if i < temp:
                    temp = i
                    
        return temp
