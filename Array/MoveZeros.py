class Solution1(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        c = 0
        for n in nums:
            if n != 0:
                nums[c]=n
                c +=1
        while(c<len(nums)):
            nums[c] = 0
            c+=1

class Solution2(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        for n in nums:
            if n == 0:
                nums.remove(n)
                nums.append(n)
