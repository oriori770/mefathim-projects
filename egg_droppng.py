import math
import timeit
def egg_drop(k, n):
    """
        Returns the minimum number of trials needed to determine the critical floor
        using k eggs and a building with n floors.

        Args:
          k: The number of eggs.
          n: The number of floors.

        Returns:
          The minimum number of trials needed.
        """

    # Base cases
    if n == 1:
        return 1
    if k == 1:
        return n
    if math.log(n) < k:
        return math.log(n)

    # Create a table to store the minimum number of trials needed for
    # each combination of eggs and floors.
    matrix = [[0 for column in range(n + 1)] for line in range(k + 1)]
    # Initialize the table.
    # We always need i trials for one egg and i floors.
    for i in range(n + 1):
        matrix[1][i] = i
    # We need one trial for one floor
    for i in range(k + 1):
        matrix[i][1] = 1

    for egg in range(2, k + 1):
        for floor in range(2, n + 1):
            min_of_max = float('inf')
            for j in range(2, floor + 1):
                maximum = max(matrix[egg - 1][j - 1], matrix[egg][floor - j]) + 1
                if maximum < min_of_max:
                    min_of_max = maximum
            matrix[egg][floor] = min_of_max
    return matrix[k][n]


print(egg_drop(5, 1000))
