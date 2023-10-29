from statistics import mode
class Constitution:
    def __init__(self):
        pass

    def __repr__(self):
        pass

    def add_rule(self, rule):
        pass

    def remove_rule(self, rule):
        pass


class Minister:
    def __init__(self, name, party):
        self.name = name
        self.party = party

    def add_rule(self, rule, constitution: Constitution, *args, **kwargs):
        constitution.add_rule(rule)
        print(f'A new rule by {self.name} was accepted')

    def cancel_rule(self, rule, constitution):
        constitution.remove_rule(rule)
        print(f'rule was canceled by {self.name}')


class ActingMinister(Minister):
    def __init__(self, name, party, minister_name: str):
        super().__init__(name, party)
        self.minister_name = minister_name.upper()

    def add_rule(self, rule, constitution, votes: list = None, *args, **kwargs):
        if sum(votes) > len(votes) / 2:
            super().add_rule(rule, constitution, *args, **kwargs)

    def cancel_rule(self, rule: str, constitution):
        if self.minister_name in rule.upper():
            super().cancel_rule(rule, constitution)
        else:
            raise ValueError('rule was accepted')


a = Constitution()
c = Minister('gfg', 'gff')
c.add_rule('ded', a)


# a = [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1]
# print(sum(a))


def most_productive_ministry(dict_of_rule: dict):
    dict_of_rule = dict_of_rule.values()
    cunter = {}
    for minister in dict_of_rule:
        if minister in cunter:
            cunter[minister] += 1
        else:
            cunter[minister] = 1
    return max(cunter, key=cunter.get)


a = {'rule1': 'a1', 'rule2': 'a1', 'rule3': 'a2', 'rule4': 'a2', 'rule5': 'a2'}
print(a.get('a'))
# a = a.values()
print(set(a))
# a['rule1'] = 2
print(a)
# a['rule9'] = 3
print(a)
v = most_productive_ministry(a)
print(v)
# print(a.get('rule3'))
# print(max(a, key=a.get))
# print(max(a))
print(mode(a.values()))