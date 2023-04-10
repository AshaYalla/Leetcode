class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        look={"(":")","{":"}","[":"]"}
        
        for i in s:
            if i in look:
                stack.append(i)
            else:
                if(len(stack) != 0):
                    a = stack.pop()
                    if i == look[a]:
                        pass
                    else:
                        return False
                else:
                    return False
        return len(stack) == 0 
                