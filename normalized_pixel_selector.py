from default_pixel_selector import PixelSelector
from normalized_selector import NormalizedSelector


class NormalizedPixelSelector(PixelSelector, NormalizedSelector):
    def __init__(self, data, track_weight=False):
        super().__init__(data)
        self.weight = 0
        self.track_weight = track_weight

    def random_selection(self):
        return super().random_selection()

    def _compute_and_set_weight(self):
        if self.isLeafNode():
            x_range = self.data.get("x_limits")[
                1] - self.data.get("x_limits")[0]
            y_range = self.data.get("y_limits")[
                1] - self.data.get("y_limits")[0]
            self.weight = x_range * y_range
        else:
            self.weight = sum([child.get_weight()
                              for child in self.children])
