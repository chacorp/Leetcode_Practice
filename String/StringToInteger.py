class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        a=0
        b=0
        n=""
        
        u=1
        z=ord('0')
        lim=-2**(31)
        
        for i,w in enumerate(s):
            if b>1:
                break
            if len(n)>0:
                if 48> ord(w) or ord(w)> 57:
                    break
            if len(n)<1 and w=='0':
                    continue
            if 47< ord(w) < 58:
                n= n+w
                if len(n)>10:
                    if u>0:
                        return -(lim+1)
                    else:
                        return lim
            else:
                if w==" ":
                    if i > 0 and s[i-1] != " ":
                        break
                    continue
                elif w=="-":
                    b=b+1
                    u=-1
                    if i > 0 and s[i-1] != " ":
                        break
                elif w=='+':
                    b=b+1
                elif w==".":
                    break
                else:
                    break
            
        for w in n:
            if a*u <= (lim/10)+1 and ord(w)-z >=8:
                return lim
            if a*u > -lim/10:
                return -(lim+1)
            if a*u >= -lim/10 and ord(w)-z >=-lim%10:
                return -(lim+1)
            a = a*10 + ord(w)-z
        return a*u
