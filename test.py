class Aa:
    def __init__(self, size):
        self.one = size
        self.too = 2

    def __len__(self):
        return len(str(self.one))

    def __str__(self):
        return f'*{self.too}, {self.one}*'

    def foo(self):
        a = [1, 3, 5]
        return a


test = Aa('shneor')


# print(test.foo())


class Bb(Aa):
    def __init__(self, size, wide):
        super().__init__(size)
        self.trre = 3
        self.wide = wide

    def foo(self):
        t = super().foo()
        t.append(5)
        return t


test = Bb('shneor', 6)
# print(test.foo())

first = Aa(777)
scend = Bb(7, 8)


# print(scend.one)
# print(scend.wide)
# print(first)
# print(len(first))

class Car:
    def __init__(self, model):
        self.model = model

    def say_hello(self):
        return f"Hello, I'm a {self.model}"


class SportsCar(Car):
    def __init__(self, sports_engine, model):
        super().__init__(model=model)
        # self.sports_engine = sports_engine

    def over_drive(self):
        return f"Smashing it!! With my {self.sports_engine} engine"

    def say_hello(self):
        super().say_hello()


sportsCar1 = SportsCar('V8', 2007)
# print(sportsCar1.say_hello())
# print(sportsCar1.over_drive())
# print(sportsCar1.model)
a = [3, 6, 85, 3, 7, 8, 3, 9]
aa = {3, 3, 3, 3, 3, 3, 3, 9}
a90 = ['fdf', 'uiui','h','uiuihguihiu']
# a = {'rule1': 3, 'rule2': 3, 'rule3': 2, 'rule4': 22, 'rule5': 10}
# a['rule6'] = 1
# print(a)

# b = a.copy()
# print(a)
# a.pop()
# print(a)
# print(b)
# print(a)
# g = sorted(a)[:3]
# print(g)
# print(a['rule1'])
jj = [1,2, 3]
*gg, jll =jj
print(jll)
print(a)
v = [5,6]
# a.append(v)
# print(a)
a.extend(v)
print(a)