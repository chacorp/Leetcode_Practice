class Solution1(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = None
        
        while (a == None):
            ms= [nu-nums[0] for nu in nums]            
            #print('ms',ms)

            # 0인 인덱스 찾기
            idx = [i for i,m in enumerate(ms) if m==0 ]
            #print(idx)

            # 0 이 하나만 있을 경우
            if len(idx)==1:
                a = nums[idx[0]]
                
            # 0 이 여러개
            else :
                idx.reverse()
                for e in idx:
                    nums.pop(e)
                print('nums',nums)
        return a


class Solution2(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = None
        b=0
        
        while (a == None):
            temp = nums[b]
            nums= [n-temp for n in nums]            
            #print('ms',ms)

            # 0인 인덱스 찾기
            idx = [i for i,m in enumerate(nums) if m==0 ]
            #print(idx)

            # 0 이 하나만 있을 경우
            if len(idx)==1:
                a = nums[idx[0]]+temp
                print(idx[0])
            # 0 이 여러개
            else :
                nums= [n+temp for n in nums]
                b +=1
        return a
    
class Solution3(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = None
        while (a == None):
            # 같은 거 갯수 카운터
            c=0
            # 처음 하나 가져오기
            t=nums[0]
            
            # 나머지와 비교하기
            for n in nums:
                if t==n:
                    c+=1 
            # 같은게 없으면 출력하기
            if c == 1:
                a=t
            else:
                nums.remove(t)
                nums.remove(t)
        return t
