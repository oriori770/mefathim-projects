from MyStack import MyStack
import random

class Min_Stack(MyStack):

    def __init__(self):
        super().__init__()
        self.min = Min_Stack()

    def push(self, element=None):
        super().push(element)
        if self.min.is_empty()