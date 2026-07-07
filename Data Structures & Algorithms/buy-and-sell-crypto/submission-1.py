class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr_profit=0
        profit=0
        buy_price=prices[0]
        for i in range(1,len(prices)):
            if(prices[i]<buy_price):
                buy_price=prices[i]
            else:
                curr_profit=prices[i]-buy_price
                profit=max(profit,curr_profit)
        return profit



        