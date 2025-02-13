# Problem: Maximum Ice Cream Bars - https://leetcode.com/problems/maximum-ice-cream-bars/

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        ans=0
        for i in costs:
            if(coins-i>=0):
                ans+=1
                coins-=i
            else:
                break
        return ans

        