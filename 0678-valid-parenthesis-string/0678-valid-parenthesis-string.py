# class Solution:
#     # Ok, there is another solution. First, we need to remove all the matching parenthesis using classical stack-based validation code.
#     # Then let's put s = stack and do the second and quite similar operation on s but this time keep track of two stacks - stack of parenthesis and stack of stars:
#     # And the final stage is to drain the parens stack trying to match it with remaining stars:
#     #     The overall time complexity is O(n) and extra memory required is also O(n).
    
#     def checkValidString(self, s):
#         stack = []
#         for c in s:
#             if c in '(*':
#                 stack.append(c)
#             elif c == ')':
#                 if stack and stack[-1] == '(':
#                     stack.pop()
#                 else:
#                     stack.append(c)

#         stars = []
#         parens = []

#         for i, c in enumerate(stack):
#             if c == '*':
#                 stars.append((i, c))
#             elif c == '(':
#                 parens.append((i, c))
#             else:  # c == ')'
#                 if parens:
#                     parens.pop()
#                 elif stars:
#                     stars.pop()
#                 else:
#                     return False

#         while parens:
#             i, c = parens.pop()
#             if not stars:
#                 return False
#             if stars[-1][0] < i:
#                 return False
#             stars.pop()        

#         return True

# class Solution:
#     def checkValidString(self, s: str) -> bool:
        
#         # store the indices of '('
#         stk = []
        
#         # store the indices of '*'
#         star = []
        
        
#         for idx, char in enumerate(s):
            
#             if char == '(':
#                 stk.append( idx )
                
#             elif char == ')':
                
#                 if stk:
#                     stk.pop()
#                 elif star:
#                     star.pop()
#                 else:
#                     return False
            
#             else:
#                 star.append( idx )
        
        
#         # cancel ( and * with valid positions, i.e., '(' must be on the left hand side of '*'
#         while stk and star:
#             if stk[-1] > star[-1]:
#                 return False
        
#             stk.pop()
#             star.pop()
        
        
#         # Accept when stack is empty, which means all braces are paired
#         # Reject, otherwise.
#         return len(stk) == 0



class Solution:
    def checkValidString(self, s: str) -> bool:
        leftmax, leftmin = 0,0
        for i in s:
            if i == '(':
                leftmax +=1
                leftmin +=1
            elif i == ')':
                leftmax -=1
                leftmin = max(leftmin-1,0)
            else:
                leftmax +=1
                leftmin = max(leftmin-1,0)
            if leftmax < 0:
                return False
        return leftmin == 0
                
                
                