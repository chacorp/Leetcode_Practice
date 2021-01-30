class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # 중복된거 제거하기
        ss = set(s)
        st = set(t)
        
        # 중복 제거한 것들 각각을 본래 list에서 갯수 세기
        cs = {i: s.count(i) for i in ss}
        ct = {j: t.count(j) for j in st}        
        
        # 중복 제거한 결과가 같으면
        if ss == st:
            # 아무거나 글자 뽑아서 비교
            for w in ss:
                if cs[w] != ct[w]:
                    return False
            return True
        else:
            return False
