
class Solution2:
    def evalRPN(self, tokens: list[str]) -> int:
        """
        Refactored version
        """
        nums_stack = []
        for item in tokens:
            if item.lstrip('-').isdigit():
                nums_stack.append(int(item))
            else:
                num1, num2= nums_stack.pop(), nums_stack.pop()
                match item:
                    case '+':
                        nums_stack.append(num2 + num1)
                    case '-':
                        nums_stack.append(num2 - num1)
                    case '*':
                        nums_stack.append(num2 * num1)
                    case '/':
                        nums_stack.append(int(num2 / num1))
        return nums_stack[0]


class Solution1:
    def evalRPN(self, tokens: list[str]) -> int:
        """
        Less checks but more repeated
        """
        nums_stack = []
        for item in tokens:
            match item:
                case '+':
                    num1, num2= nums_stack.pop(), nums_stack.pop()
                    nums_stack.append(num2 + num1)
                case '-':
                    num1, num2= nums_stack.pop(), nums_stack.pop()
                    nums_stack.append(num2 - num1)
                case '*':
                    num1, num2= nums_stack.pop(), nums_stack.pop()
                    nums_stack.append(num2 * num1)
                case '/':
                    num1, num2= nums_stack.pop(), nums_stack.pop()
                    nums_stack.append(int(num2 / num1))
                case _:
                    nums_stack.append(int(item))
        return nums_stack[0]
