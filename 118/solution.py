class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        finalList = []
        while numRows > 0: 
            generateList = finalList[-1] if len(finalList) > 0 else [] 
            finalList.append(transition(generateList)) 
            numRows -= 1 
        return finalList

def transition(generateList: List[int]) -> List[int]:
    if len(generateList) == 0: 
        return [1]
    if len(generateList) == 1: 
        return [1,1]
    transitionState = [1]
    for i in range(len(generateList)-1): 
        currentSum = generateList[i] + generateList[i + 1] 
        transitionState.append(currentSum) 
    transitionState.append(1) 
    return transitionState