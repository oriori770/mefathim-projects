from typing import Any


class MyStack:
    """A class representing a stack data structure."""

    def __init__(self, capacity=float('inf')):
        """Initialize an empty stack."""
        self.array = []
        self.capacity = capacity

    def push(self, element=None) -> bool:
        """Push an element onto the stack.

        Args:
            element: The element to be pushed onto the stack.

        Returns:
            bool: True if the element was successfully pushed, False otherwise.
        """
        if element is not None and self.size() < self.capacity:
            self.array.append(element)
            return True
        return False

    def pop(self) -> Any:
        """Remove and return the top element from the stack.

        Returns:
            Any: The top element of the stack.
        """
        if self.size() > 0:
            return self.array.pop()

    def peek(self) -> Any:
        """Return the top element from the stack without removing it.

        Returns:
            Any: The top element of the stack.
        """
        if self.size() > 0:
            return self.array[-1]

    def is_empty(self) -> bool:
        """Check if the stack is empty.

        Returns:
            bool: True if the stack is empty, False otherwise.
        """
        return not self.size()

    def size(self) -> int:
        """Return the number of elements in the stack.

        Returns:
            int: The number of elements in the stack.
        """
        return len(self.array)

    def clear(self) -> None:
        """Remove all elements from the stack."""
        self.array.clear()

    def __str__(self):
        return self.array.__str__()


def checks_nested(string_parenthesis: str):
    stack = MyStack()
    open_ls = ['(', '{', '[']
    for parenthesis in string_parenthesis:
        if parenthesis in open_ls:
            stack.push(parenthesis)
        elif (parenthesis == ')' and '(' == stack.peek() or parenthesis == '}' and
              '{' == stack.peek() or parenthesis == ']' and '[' == stack.peek()):
            stack.pop()
        else:
            return False
    if not stack.is_empty():
        return False
    return True


def test(func):
    legals = ['(()[[]][])',
              '[[]{}{{}}]',
              '{[]{[][]}}',
              '()((){[]})',
              '{([][]{})}',
              '[[][()]]{}',
              '(([]{[]}))',
              '[]{[[]{}]}',
              '{[[]]{}}()',
              '{{}}[{()}]']
    illegal = ['}}))[{)({]',
               '{)({([)){}',
               '{{}[((]}}]',
               '[){{{{{)}(',
               '{}[[}]}(]{',
               '}[]]{[})[{',
               '][[([}[)()',
               '[)(]){]}(]',
               '(]}}[)})]]',
               '[)((])]{(}']
    for s in legals:
        assert func(s), s
    for s in illegal:
        assert not func(s), s
    print('yuor a king')


# test(checks_nested)
a = MyStack(3)
a.push(3)
a.push(5)
a.push(7)
a.push(4)
a.push(4)
print(a)
