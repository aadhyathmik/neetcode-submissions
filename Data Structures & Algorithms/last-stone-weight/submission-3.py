class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        stones.sort()
        
        if len(stones) == 1:
            return stones[0]

        s1 = stones[-1]
        s2 = stones[-2]

        stones.pop()
        stones.pop()

        if s2 < s1:
            stones.append(s1 - s2)
        elif s1 < s2:
            stones.append(s2 - s1)
        else:
            stones.append(0)

        return self.lastStoneWeight(stones)

            
