class Solution:
    def countSeniors(self, details: List[str]) -> int:
        return len([i[10] for i in details if int(i[11: 13]) > 60])