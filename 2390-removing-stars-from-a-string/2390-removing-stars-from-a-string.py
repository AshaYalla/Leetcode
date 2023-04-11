class Solution:
    def removeStars(self, s: str) -> str:
        s_list = list(s)
        output = []
        for letter in s_list:
            if letter != "*":
                output.append(letter)
            else:
                output.pop()
        return "".join(output)
                
        
        