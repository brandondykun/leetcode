from solution import MinStack

print("Tests - 155. Min Stack: ")


#### Example 1:
minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
min = minStack.getMin()  # return -3
print(min == -3)
minStack.pop()
top = minStack.top()  # return 0
print(top == 0)
min = minStack.getMin()  # return -2
print(min == -2)

#### Example 2 (extra):
minStack = MinStack()
minStack.push(1)
minStack.push(2)
minStack.push(3)
minStack.push(4)
minStack.push(5)
top = minStack.top()
print(top == 5)
min = minStack.getMin()  # return 1
print(min == 1)
minStack.pop()
top = minStack.top()  # return 4
print(top == 4)
minStack.push(-1)
top = minStack.top()
print(top == -1)
min = minStack.getMin()  # return -1
print(min == -1)
minStack.pop()
min = minStack.getMin()  # return 1
print(min == 1)
