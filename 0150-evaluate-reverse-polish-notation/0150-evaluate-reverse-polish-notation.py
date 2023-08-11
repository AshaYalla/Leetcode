class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operaters = ["+","-","*", "/"]
        numarr = []
        for i in tokens:
            if i not in operaters:
                numarr.append(i)
            else:
                b = numarr.pop()
                a = numarr.pop()
                if i == '+':
                    numarr.append(int(a)+int(b))
                elif i == '-':
                    numarr.append(int(a)-int(b))
                elif i == '/':
                    numarr.append(int(int(a)/int(b)))
                elif i == '*':
                    numarr.append(int(a) * int(b))
        return int(numarr[-1])
                
                    
                
            
            
        