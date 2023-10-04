class multifilter:
    def judge_half(pos, neg):
        if pos >= neg:
            return True
    def judge_any(pos, neg):
        if pos >= 1:
            return True
    def judge_all(pos, neg):
        if neg == 0:
            return True
    def __init__(self, iterable, *funcs, judge=judge_any):
        self.iterable = iterable
        self.funcs = funcs
        self.judge = judge
    def __iter__(self):
        for x in self.iterable:
            pos = 0
            neg = 0
            for f in self.funcs:
                if f(x):
                    pos += 1
                else:
                    neg += 1
            if self.judge(pos, neg):
                yield x

