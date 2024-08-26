# Recusion Approach
class Solution:
    def generateParenthesis(self, n):
        stack = []
        res = []

        def backtrack(openN, closedN):
            if openN == closedN == n:
                res.append("".join(stack))
                return

            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closedN) # Recursive call
                stack.pop()
            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN + 1) # Recursive call
                stack.pop()

        backtrack(0, 0)
        return res
