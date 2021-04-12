class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row = len(grid)
        col = len(grid[0])
        
        t_c=0
        no_z=0
        
        if row==1 and col==1:
            return 1 if grid[0][0]=="1" else 0
        
        for y in range(row):
            for x in range(col):
                count=1
                if grid[y][x]=="1":                                        
                    # 바로 앞에 거 확인해서 0이면
                    # if x!=col-1:
                    #     if grid[y][x+1]=="1":
                    #         count = 0
                        # if grid[y][x+1]=="0":
                        #     count = 1
                        
                    # 바로 위에 거 확인해서 1이면
                    if y!=0:
                        if grid[y-1][x]=="1":
                            count = 0
                        # if grid[y-1][x]=="0":
                        #     count = 1
                        
                    #혹은 바로 뒤에서 확인해서 1이면
                    if x!=0:
                        if grid[y][x-1]=="1":
                            count = 0
                    # if y!=row-1:
                    #     if grid[y+1][x]=="1":
                    #         count = 0
                    
                    t_c = t_c+1 if count > 0 else t_c
                    print(y,'\t', x,'\t count:', count, '\t total', t_c)
                    
                if grid[y][x]=="0": 
                    no_z=0
                else:
                    no_z=1
            # break
            t_c = no_z if t_c==0 and no_z!=0 else t_c
        return t_c
##################################################
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row = len(grid)
        col = len(grid[0])
                     
        t_c = 0
                
        for y in range(row):
            for x in range(col):
                # 현재 칸이 1이면 일단 ++1
                if grid[y][x]== "1":
                    t_c = t_c +1
                    # 현재 칸 아틀란티스 해버리기
                    self.eraser(grid, y, x, row, col)
        return t_c
    
    def eraser(self, grid, y, x, row, col):            
        # 경계선이면 리턴
        if y<0 or x<0 or x>=col or y>=row:
            return
        # 바다라면 리턴
        if grid[y][x]=="0":
            return
        # 그외 == 땅인 경우 모두 바다로 가라앉힘
        grid[y][x]="0"
        
        # 상하좌우 연좌제 적용하기
        self.eraser(grid, y-1, x, row, col)
        self.eraser(grid, y+1, x, row, col)
        self.eraser(grid, y, x-1, row, col)
        self.eraser(grid, y, x+1, row, col)
