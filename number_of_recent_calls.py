# Identify a pattern.
class RecentCounter:
    def __init__(self):
        self.queue = []
        self.miliseconds = 3000

    def ping(self, t:int) -> int:
        self.queue.append(t)        
        while self.queue[0] < t-self.miliseconds:
            self.queue.pop(0)
        return len(self.queue)

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
        


if __name__ == '__main__':

    counter = RecentCounter()
    result_1 = counter.ping(1)
    print(result_1)
    result_2 = counter.ping(100)
    print(result_2)
    result_3 = counter.ping(3001)
    print(result_3)
    result_4 = counter.ping(3002)
    print(result_4)

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)