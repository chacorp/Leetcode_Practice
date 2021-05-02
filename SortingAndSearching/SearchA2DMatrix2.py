import numpy as np
class Solution1:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        return np.sum(np.array(matrix) == target)
   

class Solution2:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        a=0
        for y in matrix:
            for x in y:
                if x==target:
                    a +=1       
        return a
