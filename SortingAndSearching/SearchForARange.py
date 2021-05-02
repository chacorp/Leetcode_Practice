class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # 안에 있으면...!
        idx = nums.index(target) if target in nums else -1
        # 없으면 탈락!
        if idx == -1:
            return[-1,-1]
        
        idx_i = idx
        for i in range(idx+1, len(nums)):
            if nums[i]==target:
                idx_i = i
            else:
                break
        return [idx, idx_i]
