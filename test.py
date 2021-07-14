class test:
    q: int
    w: int
    def __init__(self, q, w) -> None:
        self.q  = q
        self.w = w

w = test(1,2)
w.w = 3
print(w.w)

class test_2:
    q: int
    w: int
    def __init__(self, q, w) -> None:
        self.q  = q
        self.w = w

e = test_2(1,2)
print(e.w)