class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        area = length * width * height
        is_bulky = length >= 10**4 or width >= 10**4 or height >= 10**4 or mass >= 10**4 or area >= 10**9
        is_heavy = mass >= 100

        if is_bulky and is_heavy:
            return "Both"
        if is_bulky:
            return "Bulky"
        if is_heavy:
            return "Heavy"
        return "Neither"