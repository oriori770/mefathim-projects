class Node_Dijkstra:
    def __init__(self, x, y):
        self.parent = None
        self.neighbors = []
        self.weight = float('int')
        self.node = x, y
        self.is_wite = False
