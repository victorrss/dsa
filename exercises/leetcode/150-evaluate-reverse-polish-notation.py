class Solution:
    # TC: n
    # SC: n
    def evalRPN(self, tokens: List[str]) -> int:
        ops = set(["+", "-", "*", "/"])
        stack = []
        for t in tokens:
            if t in ops:
                n1 = stack.pop()
                n2 = stack.pop()
                stack.append(int(eval(str(f"{n2}{t}{n1}"))))
            else:
                stack.append(t)
        return int(stack[-1])
