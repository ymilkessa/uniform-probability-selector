import random
from abc import ABCMeta
from default_selector import DefaultSelector, BaseSelector


class PixelSelector(BaseSelector, metaclass=ABCMeta):
    def __init__(self, data):
        super().__init__(data)

    def _get_something(self):
        if not self.isLeafNode():
            raise Exception("This is not a leaf node")
        x_limits = self.data.get("x_limits")
        y_limits = self.data.get("y_limits")
        x_value = random.randint(x_limits[0], x_limits[1])
        y_value = random.randint(y_limits[0], y_limits[1])
        return (x_value, y_value)

    @classmethod
    def build_tree_from_list(cls, display_list):
        """
        A display_list is a list that contains tuples of the form (x_min, x_max, y_min, y_max) or other display_lists.
        This function will take in a list and recursively create a child tree for each display_list and a leaf node
        for each tuple.
        :param display_list: A list of display_lists and tuples
        :return: A tree of nodes in the form of the current class.
        """
        root = cls(None)
        for display in display_list:
            if isinstance(display, tuple):
                x_min, x_max, y_min, y_max = display
                data = {"x_limits": (x_min, x_max), "y_limits": (y_min, y_max)}
                root.add_child(cls(data))
            else:
                root.add_child(cls.build_tree_from_list(display))
        return root


class DefaultPixelSelector(DefaultSelector, PixelSelector):
    def __init__(self, data):
        super().__init__(data)
