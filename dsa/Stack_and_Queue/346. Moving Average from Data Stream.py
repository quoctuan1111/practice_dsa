class MovingAverage(object):

    def __init__(self, size):
        """
        :type size: int
        """
        self.queue = deque()
        self.total = 0
        self.size = size

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        self.queue.append(val)
        self.total += val

        if len(self.queue) > self.size:
            removed = self.queue.popleft()
            self.total -= removed
        return self.total / float(len(self.queue))


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)