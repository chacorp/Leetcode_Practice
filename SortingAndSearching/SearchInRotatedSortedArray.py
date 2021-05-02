# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         # 첫 번째 숫자가 뭐냐
#         rot = nums[0]
#         # 첫 번째 숫자번째의 위치를 기준으로 컷
#         len_front = len(nums[:rot])
#         len_back =  len(nums[rot:])
#
#         # 맨 뒤랑 같나?
#         if target == nums[-1]:
#             return len(nums)-1
#
#         # 맨 앞이랑 같나?
#         if target == rot:
#             return 0
#
#         # 첫번째 숫자보다 작은 경우엔, 첫번째 숫자번째 위치에서 시작
#         elif target < rot:
#             for i in range(len_back):
#                 if target != nums[rot]:
#                     rot=rot+1
#                 else:
#                     return rot
#             return -1
#
#         # 아니면 걍 앞에서 시작
#         elif target > rot:
#             rot = 0
#             for i in range(len_front):
#                 if target != nums[rot]:
#                     rot=rot+1
#                 else:
#                     return rot
#             return -1
