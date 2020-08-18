class Stack:
  def __init__(self):
    self.arr = []
    self.length = 0
  
  def __str__(self):
    return str(self.__dict__)
  
  def peek(self):
    return self.arr[self.length-1]

  def push(self,value):
    self.arr.append(value)
    self.length += 1

  def pop(self):
    popped_item = self.arr[self.length-1]
    del self.arr[self.length-1]
    self.length -= 1
    return popped_item

  def isEmpty(self):
    if self.length == 0:
      print(True)
    else:
      print(False)

  def getMin(self):
    print(min(self.arr))

s = Stack()
s.push(1)
s.push(2)
s.push(3)
s.push(0)
s.push(8)
s.push(7)
s.pop()
print(s)
s.isEmpty()
s.getMin()
