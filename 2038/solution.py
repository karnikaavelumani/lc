class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        counter_a = 0
        counter_b = 0
        for i in range(len(colors) - 2):
            window = colors[i:i+3]
            if window == "AAA":
                counter_a += 1
            if window == "BBB":
                counter_b += 1
        if counter_a <= counter_b:
            return False
        return True
