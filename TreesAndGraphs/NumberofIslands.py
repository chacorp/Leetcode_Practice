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
