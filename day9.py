class Counter:
    def __init__(self, initValue=0):
        self.count = initValue

    def increment(self):
        self.count += 1

    def __str__(self):
        msg = "카운트 값" + str(self.count)
        return msg

a = Counter(100)
print(a)