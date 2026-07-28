class Solution:
    def calPoints(self, operations: List[str]) -> int:
        score = []

        for n in range(len(operations)):
            if operations[n] == "+":
                score.append(int((score[-1] + score[-2])))
            elif operations[n]  == "D":
                score.append(int(score[-1]*2))
            elif operations[n]  == "C":
                score.pop()
   
            else:
                score.append(int(operations[n]))
            print(score)

        return sum(score)