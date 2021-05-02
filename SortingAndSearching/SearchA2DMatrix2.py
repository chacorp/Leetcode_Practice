import numpy as np
class Solution1:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        mat=np.array(matrix)
        a = mat == target
        a = np.sum(a)
        return a
   

class Solution2:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        a=0
        for y in matrix:
            for x in y:
                if x==target:
                    a +=1       
        return a
