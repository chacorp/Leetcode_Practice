class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = 0        
        while(a+1 < len(nums)):
            # 지금 숫지랑 다음 숫자랑 같으면 다음꺼 뽑기
            if nums[a] == nums[a+1]:
                nums.pop(a+1)
            # 지금 숫자랑 다음 숫자랑 다르면 한 칸 옮기기
            else:
                a += 1
        
        return len(nums)
