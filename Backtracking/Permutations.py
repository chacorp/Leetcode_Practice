class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        cur = []
        
        self.bababa(nums, res, cur)
        return res
        
    def bababa(self, nums, result, current):
        if len(nums)==len(current):
            result.append(current.copy())
            return
        else:
            for num in nums:
                if not (num in current):
                    current.append(num)
                    self.bababa(nums, result, current)
                    current.pop()
