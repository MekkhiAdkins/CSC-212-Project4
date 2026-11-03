"""
Author: Mekkhi Adkins
Course: CSC 212 - Data Structures
Assignment: Project 4 - Stacks
Description: Evaluate postfix expressions using a stack.
"""


# Creating the blueprint for the stack objects
class Stack:
    """Represent a stack using a Python list."""

    # constructor that runs when a stack object is created
    def __init__(self):
        """Create an empty stack."""
        # the double underscore discourages accidental access from outisde the class
        self.__items = []

    # creating a method that accepts an item to add to the stack
    def push(self, item):
        """Adds the value to the end of the objects list, which represents the top of the stack. """
        self.__items.append(item)

    def pop(self):
        """ Removes and return the top of the stack, which represents the last value added. """
        return self.__items.pop()

stack1 = Stack()

stack1.push(3)
stack1.push(5)
stack1.push(1)

print(stack1.pop())
print(stack1.pop())
print(stack1.pop())

