class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        temp = []
        a = -1 if x<0 else 1
        
        x = a*x
        while x/10 or x%10:
            temp.append(x%10)
            x=x/10
            
        temp.reverse()
        print(temp)
        
        while len(temp):
            x=x*10
            x=x+temp.pop()
            if x < -2**(31) or x>2**(31)-1:
                return 0
        x = a*x
        return x
