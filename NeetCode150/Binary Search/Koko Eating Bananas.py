class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        MIN , MAX = 1 , max(piles)
        res = MAX
        while MIN <= MAX:
            k = (MIN+MAX)//2
            hr = 0
            for pile in piles:
                hr += math.ceil(pile/k)
            if hr <= h:
                res = min(res,k)
                MAX = k-1

            else:
                MIN = k+1
        return res

        
