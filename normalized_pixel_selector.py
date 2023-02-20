import random
from default_pixel_selector import DefaultPixelSelector


class NormalizedPixelSelector(DefaultPixelSelector):
    def __init__(self, data, track_weight=False):
        super().__init__(data)
        self.weight = 0
        self.track_weight = track_weight

    def add_child(self, child):
        super().add_child(child)
        if self.track_weight:
            self.weight += child.weight

    def random_selection(self):
        if self.isLeafNode():
            return self.get_something()
        if not self.track_weight:
            self.set_and_return_weight()
        random_index = random.randint(1, self.weight+1)
        index_cursor = 0
        for child in self.children:
            index_cursor += child.weight
            if index_cursor >= random_index:
                return child.random_selection()
        raise Exception(
            "Something went wrong in random_selection: please ensure that the weights of the child nodes add up to the total weight.")

    def set_and_return_weight(self):
        if self.track_weight:
            return self.weight
        if self.isLeafNode():
            x_range = self.data.x_limits.max - self.data.x_limits.min
            y_range = self.data.y_limits.max - self.data.y_limits.min
            self.weight = x_range * y_range
        else:
            self.weight = sum([child.set_weight() for child in self.children])
        self.track_weight = True
        return self.weight

    @classmethod
    def build_tree_from_list(cls, display_list):
        root = super().build_tree_from_list(display_list)
        root.set_and_return_weight()
        return root
