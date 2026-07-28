class Solution:
    def calPoints(self, operations: List[str]) -> int:
        score = []
        prev1, prev2 = 0,0

        for n in range(len(operations)):
            if operations[n] == "+":
                score.append(int((score[prev1] + score[prev2])))
            elif operations[n]  == "D":
                score.append(int(score[prev1]*2))
            elif operations[n]  == "C":
                score.pop()
                prev1 -= 1
                prev2 -= 1
            else:
                score.append(int(operations[n]))
            
            prev2 = len(score)-2
            prev1 = len(score)-1
            print(score)

        output = 0
        for i in score:
            output += int(i)

        return output
            