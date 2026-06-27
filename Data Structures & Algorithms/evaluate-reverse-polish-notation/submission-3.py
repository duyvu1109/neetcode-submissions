class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        exp = {
            '+',
            '-',
            '*',
            '/'
        }

        for tk in tokens:
            if tk not in exp:
                stack.append(int(tk))
            else:
                s1 = stack.pop()
                s2 = stack.pop()
                if tk == '+':
                    tmp = s2 + s1
                elif tk == '-':
                    tmp = s2 - s1
                elif tk == '*':
                    tmp = s2 * s1
                else:
                    tmp = int(s2 / s1)
                stack.append(tmp)
                print(stack)

        return stack[-1]
