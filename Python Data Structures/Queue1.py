class queueclass:
    def __init__(self):
        self.q = []

    def isEmpty(self):
        if self.q == []:
            return True
        else:
            return False

    def enqueue(self, ele):
        self.q.append(ele)

    def dequeue(self):
        if self.isEmpty():
            return -1
        else:
            return self.q.pop(0)

    def search(self, ele):
        if self.isEmpty():
            return -1
        else:
            try:
                n = self.q.index(ele)
                return n
            except ValueError:
                return -2

    def display(self):
        return self.q
