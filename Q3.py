class Solution:
    def isValid(self, s: str) -> bool:
        dict = {')': '(', ']': '[', '}': '{'}
        stack = []
        for c in s:
            if c in "({[":
                stack.append(c)
            elif stack!=[] and stack[-1]==dict[c]:
                stack.pop()
            else: 
                return False
        if stack==[]:
            return True