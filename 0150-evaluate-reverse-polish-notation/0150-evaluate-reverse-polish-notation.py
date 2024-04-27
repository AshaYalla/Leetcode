class Solution:

    def evalRPN(self, tokens: List[str]) -> int:
        operaters = ["+","-","*", "/"]
        numarr = []
        for i in tokens:
            if i not in operaters:
                numarr.append(int(i))
            else:
                b = numarr.pop()
                a = numarr.pop()
                if i == '+':
                    numarr.append(a+b)
                elif i == '-':
                    numarr.append(a-b)
                elif i == '/':
                    numarr.append(int(a/b))
                elif i == '*':
                    numarr.append(a*b)
        return numarr[-1]
                
        