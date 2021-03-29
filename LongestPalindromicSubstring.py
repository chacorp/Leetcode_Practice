class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        
        start=0
        end  =0
        
        for j in range(len(s)):
            if s[j-end: j+1] == s[j-end: j+1:-1]:
                start, end = j-end, end+1
                # print(s[i: i+l])
                
            elif j-end > 0 : 
                if s[j-end-1: j+1] == s[j-end-1: j+1:-1]:
                    start, end = j-end-1, end+2
                # print(s[i: i+l])
                
        return s[start: start+end]
