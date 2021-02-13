class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        a = len(digits)-1
        digits[a] += 1
        
        while digits[a] > 9:
            digits[a] = 0
            a -= 1
            if a < 0:
                digits.insert(0, 1)
            else:
                digits[a] += 1            
        return digits
