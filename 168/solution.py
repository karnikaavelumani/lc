class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        title = ""
        quotient = columnNumber
        while quotient != 0:
            quotient, remainder = divmod(quotient - 1, 26)
            title = chr(remainder + 65) + title 
        return title