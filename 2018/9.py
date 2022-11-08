class Node:
    def __init__(self, val):
        self._val = val
        self._next = None
        self._prev = None

    def val(self):
        return self._val

    def next(self):
        return self._next

    def prev(self):
        return self._prev

    def setNext(self, next):
        self._next = next

    def setPrev(self, prev):
        self._prev = prev

players = 459
last_marble = 7179000

curr = Node(0)
curr.setNext(curr)
curr.setPrev(curr)
scores = [0 for i in range(players)]

for i in range(1, last_marble + 1):
    if i % 23 == 0:
        for _ in range(7):
            curr = curr.prev()
        scores[i % players] += i + curr.val()

        prev = curr.prev()
        next1 = curr.next()
        prev.setNext(next1)
        next1.setPrev(prev)
        curr = next1
    else:
        next1 = curr.next()
        next2 = next1.next()
        curr = Node(i)
        curr.setPrev(next1)
        curr.setNext(next2)
        next1.setNext(curr)
        next2.setPrev(curr)

    if i % 10000 == 0:
        print(i)

print(max(scores))
