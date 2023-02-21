from abc import ABC, abstractmethod
import random


class Node(ABC):
    def __init__(self, data):
        self.data = data
        self.children = []

    @abstractmethod
    def get_something(self):
        """
        Used in a leaf note to select a value from the space of values
        represented by this node.
        """
        pass

    def add_child(self, child):
        self.children.append(child)

    def random_selection(self):
        if not self.isLeafNode():
            next_node = random.choice(self.children)
            return next_node.random_selection()
        else:
            return self.get_something()

    def isLeafNode(self):
        return not self.children
