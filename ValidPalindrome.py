class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # 글자 대문자로 바꾸기
        s = s.upper()
        
        # 아스키코드에서 숫자랑 문자에 해당하는 거만 가져오기
        t = [w for w in s if 64 < ord(w) < 91 or 47< ord(w)< 58]
        
        a = len(t)/2
        c=0
        print(t)
        while c < a:
            if t[c] != t[len(t)-1-c]:
                return False
            c=c+1
        return True
