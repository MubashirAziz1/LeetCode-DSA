class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        i = 0
        while i < len(tokens):
            if tokens[i] == '+':
                a = st.pop() + st.pop()
                st.append(a)
            elif tokens[i] == '*':
                a = st.pop() * st.pop()
                st.append(a)
            elif tokens[i] == '-':
                a = st.pop(-2) - st.pop(-1)
                st.append(a)
            elif tokens[i] == '/':
                a = st.pop(-2) / st.pop(-1)
                st.append(int(a))
            else:
                st.append(int(tokens[i]))
            
            i += 1
            
        return st[0]
        
