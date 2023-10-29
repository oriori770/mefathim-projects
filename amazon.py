class Product:
    def __init__(self, name: str, bought_with: dict = {}):
        if len(name) < 2:
            raise ValueError('invalid name')
        self.name = name
        self.bought_with = dict(bought_with)  # הוספתי את DICT על מנת ליצור עותק

    def __repr__(self):
        return f'{self.name}'

    def update(self, product_name: list):
        copy_product_name = product_name[:]  # שורה חדשה של יצירת עותק
        for item in copy_product_name:
            if item in self.bought_with:
                self.bought_with[item] += 1
            else:
                self.bought_with[item] = 1

    def get_recommendations(self, k):
        # # big_values = sorted(self.bought_with.values(), reverse=True
        # big_values = sorted(self.bought_with.items(), key=lambda x: x[1], reverse=True)
        # ls = []
        # for i in range(min(k, len(self.bought_with))):
        #     ls.append(big_values[i][0])
        #     # ls.append(self.bought_with.get(big_values[i]))
        return sorted(self.bought_with, key=a.get, reverse=True)[:min(k, len(self.bought_with))]


class GoldProduct(Product):
    def __init__(self, name: str, amount: int, bought_with: dict = {}):
        super().__init__(name, bought_with)
        # super().__init__(self, name, bought_with)
        self.amount = amount

    def __repr__(self):
        return f'{self.name} ({self.amount} units left)'

    def update(self, product_name: list):
        # super().update()
        super().update(product_name)
        self.amount -= 1

    def get_recommendations(self, k):
        # # big_values = sorted(self.bought_with.values(), reverse=True)
        # big_values = sorted(self.bought_with.items(), key=lambda x: x[1], reverse=True)
        # ls = []
        # for i in range(min(k, len(self.bought_with))):
        #     if big_values[i][1] > 9:
        #         ls.append(big_values[i][0])
        #     # ls.append(self.bought_with.get(big_values[i]))
        k_items = super().get_recommendations(k)
        gold_items = [item for item in k_items if a[item] > 9]
        return gold_items


a = {'rule1': 3, 'rule2': 3, 'rule3': 2, 'rule4': 22, 'rule5': 10}
b = [1, 5, 6, 46, 7, 8, 9, 9, 101, 4, 56, 45, 447]

# prod = Product('bag', a)
# print(prod)
# print(prod.bought_with)
# prod.update(b)
# prod.update(b)
# prod.update(b)
# print(prod.bought_with)
# print(prod.get_recommendations(10))
# prod.update(b)
# prod.update(b)
# print(prod.get_recommendations(1000))
# gold = GoldProduct('case', 100, a)
# print(gold.bought_with)
# print(gold.get_recommendations(9))
# print(a)
# prod.update(b)

# print(a)
# gold = sorted(a, key=a.get, reverse=True)[:min(4, len(b))]
# print(gold)
# gold = [item for item in gold if a[item] > 9]
# print(gold)
