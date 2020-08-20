# refer to this link
#  https://leetcode.com/problems/min-stack/discuss/201044/Python-single-stack-O(1)-all-operations 

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x: int) -> None:
        if not self.stack:
            self.stack.append(x)
        else:
            if x >= self.stack[-2]:
                self.stack.append(self.stack[-2])
            else:
                self.stack.append(x)
        self.stack.append(x)

    def pop(self) -> None:
        self.stack.pop()
        self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.stack[-2]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
