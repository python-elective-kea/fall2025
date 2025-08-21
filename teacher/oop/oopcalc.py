class F:
    def __init__(self):
        self.res = 0

    def add(self, a, b):
        self.res += sum((a,b))
        return self.res

