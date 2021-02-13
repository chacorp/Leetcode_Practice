class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        size = len(matrix)
        a = size%2
        
        # odd
        if a == 1:
            m_n = size/2
            m_x = size-1
            
            for m in range(m_n): 
                for n in range(m_n):
                    temp = matrix[m][n]
                    matrix[m][n] = matrix[m_x-n][m]
                    matrix[m_x-n][m] = matrix[m_x-m][m_x-n]
                    matrix[m_x-m][m_x-n] = matrix[n][m_x-m]
                    matrix[n][m_x-m] = temp
                    
            for m in range(m_n):
                temp = matrix[m][m_n]
                matrix[m][m_n] = matrix[m_n][m]
                matrix[m_n][m] = matrix[m_x-m][m_n]
                matrix[m_x-m][m_n] = matrix[m_n][m_x-m]
                matrix[m_n][m_x-m] = temp
            
        # even
        else:
            m_n = size/2
            m_x = size-1
            
            for m in range(m_n): 
                for n in range(m_n):
                    temp = matrix[m][n]
                    matrix[m][n] = matrix[m_x-n][m]
                    matrix[m_x-n][m] = matrix[m_x-m][m_x-n]
                    matrix[m_x-m][m_x-n] = matrix[n][m_x-m]
                    matrix[n][m_x-m] = temp
