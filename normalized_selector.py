import random
from abc import abstractmethod, ABCMeta
from default_selector import BaseSelector


class NormalizedSelector(BaseSelector, metaclass=ABCMeta):
    """Abstract class that uses weighted branch selection to pick an item"""

    def __init__(self, data):
        super().__init__(data)
        self.weight: int = 0
        self.track_weight: bool = False

    @abstractmethod
    def _compute_and_set_weight(self):
        """Set the weight of this node and return it"""
        pass

    def get_weight(self):
        """Get the weight of this node"""
        if self.track_weight:
            return self.weight
        else:
            self._compute_and_set_weight()
            self.track_weight = True
            return self.weight

    def add_child(self, child):
        super().add_child(child)
        if self.track_weight:
            self.weight += child.get_weight()

    def random_selection(self):
        if self.isLeafNode():
            return self._get_something()
        weight = self.get_weight()
        random_index = random.randint(1, weight+1)
        index_cursor = 0
        for child in self.children:
            index_cursor += child.get_weight()
            if index_cursor >= random_index:
                return child.random_selection()
        raise Exception(
            "Something went wrong in random_selection: please ensure that the weights of the child nodes add up to the total weight.")
