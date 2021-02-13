class Solution1(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        day = 0
        minP = prices[0]
        maxP = 0
        profit = 0
        
        while day < len(prices)-1:
            # 오늘이 내일보다 비쌀 경우
            if prices[day] > prices[day+1]:
                if maxP != 0:
                    profit += maxP-minP
                    maxP = 0
                    print('max',maxP)
                minP = prices[day+1]
                print('min',minP)
            # 오늘이 내일보다 쌀 경우
            if prices[day] < prices[day+1]:
                maxP = prices[day+1]
                print('max',maxP)
            #마지막 날일 경우
            if day==len(prices)-2:
                if maxP != 0:
                    profit += maxP-minP
                
            day += 1
            
        return profit

class Solution2(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        d = 1
        prev = prices[0]
        a = 0
        
        while d <= len(prices)-1:
            # 어제보다 오늘이 더 비싸다면 무조건 panda!
            if prev < prices[d]:
                a+= prices[d]-prev
            prev = prices[d]
            d += 1
                
        return a