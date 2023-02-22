from default_pixel_selector import PixelSelector
from normalized_selector import NormalizedSelector


class NormalizedPixelSelector(PixelSelector, NormalizedSelector):
    """
    A pixel coordinate selector that uses weighted branch selection.
    (Mixture of NormalizedSelector and PixelSelector.)
    """

    def set_leaf_weight(self):
        if self.isLeafNode():
            x_range = self.data.get("x_limits")[
                1] - self.data.get("x_limits")[0]
            y_range = self.data.get("y_limits")[
                1] - self.data.get("y_limits")[0]
            self.total_weight = x_range * y_range
