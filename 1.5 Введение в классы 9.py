class Buffer:
    def __init__(self):
        self.five = []
    def add(self, *a):
        for i in a:
            self.five.append(i)
            if len(self.five) == 5:
                print(sum(self.five))
                self.five = []
    def get_current_part(self):
        return self.five