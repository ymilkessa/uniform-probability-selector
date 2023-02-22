import random
from abc import abstractmethod, ABCMeta
from default_selector import BaseSelector


class NormalizedSelector(BaseSelector, metaclass=ABCMeta):
    """Abstract class that uses weighted branch selection to pick an item"""

    def __init__(self, data):
        super().__init__(data)
        self.total_weight: int = 0
        self.track_weight: bool = False
        self.weights: list[int] = []

    def _compute_and_set_weights(self):
        """Insert the weight of each child node to the self.weights, and also compute the total weight
        and set that to self.total_weight"""
        if self.isLeafNode():
            self.set_leaf_weight()
        else:
            self.weights = [child.get_weight() for child in self.children]
            self.total_weight = sum(self.weights)

    @abstractmethod
    def set_leaf_weight(self):
        """If this node is a leaf, compute and return the weight"""
        pass

    def get_weight(self):
        """Get the weight of this node"""
        if self.track_weight:
            return self.total_weight
        else:
            self._compute_and_set_weights()
            self.track_weight = True
            return self.total_weight

    def add_child(self, child):
        super().add_child(child)
        if self.track_weight:
            self.total_weight += child.get_weight()

    def random_selection(self):
        """
        Returns a randomly selected value from the tree.
        If the node has children, it will perform a weighted random selection to 
        pick a child node and then gets a random value from that child node.
        If this is a leaf node, it will call the get_something() method to get some value.
        """
        if self.isLeafNode():
            return self.get_something()
        random_child_node = random.choices(self.children, weights=self.weights)
        return random_child_node[0].random_selection()
