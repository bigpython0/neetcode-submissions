class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        while True:
            if len(stones) == 1:
                break
            l = len(stones)
            stones = sorted(stones)
            stone1 = stones[l-1]
            stone2 = stones[l-2]

            if stone1 == stone2:
                stones.remove(stone1)
                stones.remove(stone2)
            elif stone1 < stone2:
                stones[l-2] -= stone1
                stones.remove(stone1)
            else:
                stones[l-1] -= stone2
                stones.remove(stone2)
        return stones[0]

