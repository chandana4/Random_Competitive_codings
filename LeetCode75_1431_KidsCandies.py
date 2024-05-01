class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        out = [False] * len(candies)
        for i in range(0, len(candies)):
            newcandy = candies[i] + extraCandies
            count = 0
            for j in range(0, len(candies)):
                if j != i:
                    if newcandy >= candies[j]:
                        count = count + 1
            if count == len(candies) - 1:
                out[i] = True
        return out

