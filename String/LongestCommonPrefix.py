class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # one 
        if len(strs)==1:
            return strs[0]
        
        # less than one
        if len(strs)<1:
            return ""
        
        # else
        ln=len(strs)
        s=strs[0]
        for i in range(1, ln):
            ss=strs[i]
            if len(s)<= len(ss):
                print(len(s), len(ss))
                for j in range(len(s)):
                    if s[j]!= ss[j]:
                        s=s[:j]
                        break
            else:
                temp=s; s=ss; ss=temp
                print(len(s), len(ss))
                for j in range(len(s)):
                    if s[j]!=ss[j]:
                        s=s[:j]
                        break
        return s