class Solution:
    def removeStars(self, s: str) -> str:
        output = []
        for letter in s:
            if letter != "*":
                output.append(letter)
            else:
                output.pop()
        return "".join(output)
                
        
        