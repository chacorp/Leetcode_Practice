class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        
        if n==1:
            return str(n)
        else:
            a=self.countAndSay(n-1)
            b=""
            d=a[0]
            c=0
            for l in a:
                if l==d:
                    c=c+1
                else:
                    b=d+str(c)+b
                    c=1
                    d=l
            b=d+str(c)+b
        return b[::-1]
