class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        len_intervals = len(intervals)
        if len_intervals == 1:
            return intervals
          
        # sort!
        intervals.sort()
        
        print(intervals)
        # make new intervals
        new_intervals=[]
        
        #start from 0-th       
        left = intervals[0]
                
        # intervals start from 1-st
        r = 0
                
        # until len-1 because right has to be i+1
        while r < len_intervals-1:     
            # move right
            r = r+1
            right = intervals[r]
                        
            # if left[0] >= right[0] and left[1]>= right[1]:
            #     tmp = right
            #     intervals[r] = left
            #     left = tmp
            #     r = r-1
            #     continue
            
            # before
            print(left, right, end='->')
            
            # merge condition
            if left[1] >= right[0] and right[1]>= left[0]:     
                if left[0] >= right[0]:
                    left[0] = right[0]
                if left[1] <= right[1]:
                    left[1] = right[1]
                    
            elif left[1] < right[0]:
                new_intervals.append(left)
                left = right                
                
            # after
            print(left, right)
            
        new_intervals.append(left)
        return new_intervals
                
