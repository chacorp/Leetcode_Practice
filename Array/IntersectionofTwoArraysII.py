class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        s, b = None, None
        if len(nums1)<len(nums2):
            s, b = nums1, nums2 
        else:
            s, b = nums2, nums1
        
        a=[]
        while len(s)>0:        
            c = 0
            for n in b:
                if s[0] == n:
                    a.append(n)
                    b.remove(n)
                    break
            s.pop(0)
        return a
