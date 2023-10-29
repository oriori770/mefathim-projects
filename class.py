def fn_add(x):
    return x + 1


class A:
    def add(self, x):
        self.y = x + 1
        return self.y


class B:
    def __call__(self, x):
        self.y = x + 1
        return self.y


# b = B()
# print(b(10))
# print(fn_add(5))
# print(b.y)
#
# a = A()
# print(a.add(8))
# print(fn_add(5))
# print(a.y)


from collections import defaultdict


def colors():
    def log_missing():
        print('Key added')

        return 0

    current = {'green': 12, 'blue': 3}
    increments = [('red', 5), ('blue', 17), ('orange', 9)]

    result = defaultdict(log_missing, current)
    print('Before:', dict(result))
    for key, amount in increments:
        result[key] += amount
    print('After: ', dict(result))


# colors()

current = {'green': 12, 'blue': 3}
increments = [('red', 5), ('blue', 17), ('orange', 9)]


def increment_with_report(current, increments):
    added_count = 0

    def missing():
        nonlocal added_count
        added_count += 1
        return 0
        # Stateful closure

    result = defaultdict(missing, current)
    print('Before:', dict(result))
    for key, amount in increments:
        result[key] += amount
    print('After: ', dict(result))
    print(added_count)
    return result, added_count


# increment_with_report(current, increments)


class CountMissing:
    def __init__(self):
        self.added = 0

    def missing(self):
        self.added += 1

        return 0


def increment_with_report_2():
    counter = CountMissing()
    result = defaultdict(counter.missing, current)
    print('Before:', dict(result))
    for key, amount in increments:
        result[key] += amount
    print('After: ', dict(result))
    print(counter.added)
    assert counter.added == 2


# color()

class BetterCountMissing:
    def __init__(self):
        self.added = 0

    def __call__(self):
        self.added += 1
        return 0


def increment_with_report_3():
    counter = BetterCountMissing()
    result = defaultdict(counter, current)
    print('Before:', dict(result))
    for key, amount in increments:
        result[key] += amount
    print('After: ', dict(result))
    print(counter.added)
    assert counter.added == 2


# increment_with_report_3()
con = 0
def log_missing():
    # print('Key added')
    return 0


current = {'green': 12, 'blue': 3}
result = defaultdict(log_missing, current)
print(result)
result['6'] += 7
print(result)
a = {'a': 6, 'b': 8, '78': 'hjkh'}
a = defaultdict(log_missing, a)
a['c'] += 2
print(a)
print(a.keys())