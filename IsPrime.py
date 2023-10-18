def is_prime(n: int):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
        return n > 1

print(is_prime(17))
print(is_prime(15))
# print(is_prime("a"))






