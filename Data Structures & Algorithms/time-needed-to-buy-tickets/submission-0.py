class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        pos = k
        steps = 0
        while tickets[pos] != 0:
            tickets[0] -= 1
            steps += 1

            if pos == 0 and tickets[0] == 0:
                return steps
            
            current = tickets.pop(0)

            if current > 0:
                tickets.append(current)

            if pos == 0:
                pos = len(tickets)-1
            else:
                pos -= 1
