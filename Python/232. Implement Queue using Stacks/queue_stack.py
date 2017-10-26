class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack_push = []
        self.stack_pop = []
        

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        while len(self.stack_pop) > 0:
            self.stack_push.append(self.stack_pop.pop())
        self.stack_push.append(x)    
        while len(self.stack_push) > 0:
            self.stack_pop.append(self.stack_push.pop())

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        return self.stack_pop.pop()
        

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        return self.stack_pop[-1]
        

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return len(self.stack_pop) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
