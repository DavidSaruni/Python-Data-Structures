# using lists as stacks - last-in, first-out
stack = [3,4,5,6]
print(stack)
stack.append(7) #adding item to the top of stack
stack.append(8)
print(stack)
stack.pop() #pop removes the last item in to be the first item out
print(stack)
stack.pop()
print(stack)

# using lists as queues
print(" ")
print("** Lists as Queues **")
from collections import deque #deque has fast appends and pops from both ends
queue = deque(["Justine", "Nicolas", "Emmanuel"])
queue.append("Captain") # captain arrives
print(queue)
queue.appendleft("Timps") # adding to begin of queue
print(queue)
queue.pop() # the last becomes first to leave
print(queue)
queue.popleft() # the first in queue leaves
print(queue)