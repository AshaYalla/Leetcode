class Solution:
    # Ok, there is another solution. First, we need to remove all the matching parenthesis using classical stack-based validation code.
    # Then let's put s = stack and do the second and quite similar operation on s but this time keep track of two stacks - stack of parenthesis and stack of stars:
    # And the final stage is to drain the parens stack trying to match it with remaining stars:
    #     The overall time complexity is O(n) and extra memory required is also O(n).
    
    def checkValidString(self, s):
        stack = []
        for c in s:
            if c in '(*':
                stack.append(c)
            elif c == ')':
                if stack and stack[-1] == '(':
                    stack.pop()
                else:
                    stack.append(c)

        stars = []
        parens = []

        for i, c in enumerate(stack):
            if c == '*':
                stars.append((i, c))
            elif c == '(':
                parens.append((i, c))
            else:  # c == ')'
                if parens:
                    parens.pop()
                elif stars:
                    stars.pop()
                else:
                    return False

        while parens:
            i, c = parens.pop()
            if not stars:
                return False
            if stars[-1][0] < i:
                return False
            stars.pop()        

        return True