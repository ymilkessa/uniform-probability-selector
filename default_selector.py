from abc import ABCMeta, abstractmethod
import random


class BaseSelector(metaclass=ABCMeta):
    """
    Abstract class that uses random branch selection to pick a value from the tree
    """

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

    @abstractmethod
    def random_selection(self):
        pass

    def isLeafNode(self):
        return not self.children


class DefaultSelector(BaseSelector):
    def random_selection(self):
        if not self.isLeafNode():
            next_node = random.choice(self.children)
            return next_node.random_selection()
        else:
            return self.get_something()
