class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        a = True
        # 1행씩 확인하기
        for rw in board:
            for cl in rw:
                if cl == ".":
                    continue
                temp=0
                for c_l in rw:
                    if c_l == cl:
                        temp+=1
                if temp >= 2:
                    return False
                #print(cl,':', temp)
            #print('---')
            
        # 1열씩 확인하기
        for rw in board:
            for idx, cl in enumerate(rw):
                temp = 0
                if cl == ".":
                    continue
                for r_w in board:
                    if cl == r_w[idx]:
                        temp +=1
                if temp >= 2:
                    return False
                #print(cl,':', temp)
            #print('---')
        
        sub = 0
        # 3x3 확인하기
        while sub < 9:
            #print(sub,"-----")
            for n, cl in enumerate(board[sub]):
                temp = 0
                if cl==".":
                    continue
                # 9개의 3x3 중에서 어느 칸에 해당하는지 확인
                e=1 
                if n-3 < 0:
                    e = 0
                if n-3 >= 3:
                    e = 2
                d=1
                if sub-3 < 0:
                    d = 0
                if sub-3 >= 3:
                    d = 2
                
                for r_w in range(0+(d*3), 3+(d*3)):
                    for c_l in range(0+(e*3), 3+(e*3)):
                        if cl == board[r_w][c_l]:
                            temp+=1
                if temp >= 2:
                    return False
                #print(cl,':', temp)
            sub+=1
                    
        return a
