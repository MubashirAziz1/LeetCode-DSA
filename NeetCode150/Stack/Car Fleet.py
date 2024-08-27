class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        for i in range(len(position)):
            stack.append((position[i] , ((target - position[i])/speed[i])))

        stack = sorted(stack, key= lambda x: x[0] )

        n = 0
        while stack:
            if len(stack) != 1:
                if  stack[-1][1] >= stack[-2][1] :
                    stack.pop(-2)
                    continue
                else:
                    stack.pop()
                    n += 1
            else:
                n += 1
                stack.pop()
        return n
            
                
