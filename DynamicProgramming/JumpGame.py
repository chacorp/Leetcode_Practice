class Solution:
     def canJump(self, nums: List[int]) -> bool:
        len_nums = len(nums)
        # 마지막 인덱스
        last_idx = len_nums-1
        
        for idx in reversed(range(len_nums)):
            # 마지막 직전의 인덱스랑 값의 합이 
            # 마지막 값이랑 같거나 크면 그 인덱스에서 올 수 있다는 것!
            if idx + nums[idx] >= last_idx:
                last_idx=idx
        # 만약 역으로 돌아서 0번째에 도달했으면 쌉가능하다는 것
        return 1 if last_idx==0 else 0
            
## TIME LIMIT EXCEED.....!!!!
#    def canJump(self, nums: List[int]) -> bool:
#         len_nums = len(nums)
        
#         # 길이가 1이먄 뭔짓을 해도 끝!
#         if len_nums==1:
#             return 1
#         return self.johnnajump(nums, 0, len_nums-1)
            
        
#     def johnnajump(self, nums: List[int], idx: int, max_len: int) -> bool:
#         if idx == max_len:
#             return 1
        
#         jump = min(nums[idx] + idx, max_len)
        
#         # 점프
#         for next_idx in range(jump, idx, -1):
#             if self.johnnajump(nums, next_idx, max_len):
#                 return 1
#         return 0
