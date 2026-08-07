class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = ['+', '-', '*', '/']
        for val in tokens:
            if val not in ops:
                stack.append(int(val))
            else:
                if val == '+':
                    stack.append(stack.pop() + stack.pop())
                elif val == '-':
                    first = stack.pop()
                    second = stack.pop()
                    stack.append(second-first)
                elif val == '*':
                    stack.append(stack.pop() * stack.pop())
                elif val == '/':
                    first = stack.pop()
                    second = stack.pop()
                    stack.append(int(float(second)/first))

        return stack[0]