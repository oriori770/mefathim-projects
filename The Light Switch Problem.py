n = 100
n += 1
lamps = [0 for i in range(1, n)]
for dwarf in range(1, n):
    for lamp in range(n - 1):
        if (lamp + 1) % dwarf == 0 and lamps[lamp]:
            lamps[lamp] = 0
        else:
            lamps[lamp] = 1
