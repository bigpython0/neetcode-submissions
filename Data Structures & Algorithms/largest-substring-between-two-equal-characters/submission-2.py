class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        first_seen = {}
        max_len = -1
        
        for i, char in enumerate(s):
            if char in first_seen:
                # Abstand berechnen (ohne die beiden Zeichen selbst)
                max_len = max(max_len, i - first_seen[char] - 1)
            else:
                # Merke dir den ersten Auftritt dieses Zeichens
                first_seen[char] = i
                
        return max_len