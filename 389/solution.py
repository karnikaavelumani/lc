class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        freq_map = makeFreqMap(s)
        for c in t:
            if c in freq_map:
                freq_map[c] -= 1
                if freq_map[c] == 0:
                    del freq_map[c]
                continue
            return c

def makeFreqMap(s: str) -> dict:
    freq_map = {}
    for c in s:
        if c in freq_map:
            freq_map[c] += 1
        else:
            freq_map[c] = 1
    return freq_map