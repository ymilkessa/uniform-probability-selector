from default_pixel_selector import DefaultPixelSelector
from normalized_pixel_selector import NormalizedPixelSelector
from gui import Gui
import argparse
from threading import Thread

square_width = 80

display_list = [
    (0, square_width, 0, square_width),
    [
        (0, square_width, square_width, 2 * square_width),
        [
            (square_width, 2 * square_width, 0, square_width),
            [
                (2 * square_width, 3 * square_width, 0, square_width),
                [
                    (square_width, 2 * square_width,
                     square_width, 2 * square_width),
                    [
                        (0, square_width, 2 * square_width, 3 * square_width),
                        [
                            (square_width, 2 * square_width,
                             2 * square_width, 3 * square_width),
                            [
                                (2 * square_width, 3 * square_width,
                                 square_width, 2 * square_width),
                                (2 * square_width, 3 * square_width,
                                 2 * square_width, 3 * square_width)
                            ]
                        ]
                    ]
                ]
            ]
        ]
    ]
]

total_width = 3 * square_width
total_height = 3 * square_width


def main(normalized=False):
    if normalized:
        pixel_selector = NormalizedPixelSelector.build_tree_from_list(
            display_list)
        pixel_selector.get_weight()
    else:
        pixel_selector = DefaultPixelSelector.build_tree_from_list(
            display_list)

    # Get a list of 100 pixel selections
    pixel_selections = [pixel_selector.random_selection() for i in range(500)]
    print("Selections ready", len(pixel_selections))

    # Create a gui with the dimensions above
    gui = Gui(total_width, total_height)
    print("About to start marking pixels")
    # Mark the pixels in the gui
    # Run mark_pixels in a separate thread
    marking_thread = Thread(target=gui.mark_pixels, args=(pixel_selections,))
    marking_thread.start()
    gui.run_loop()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-n", "--normalized", action="store_true", help="Use normalized pixel selector")
    args = parser.parse_args()
    main(args.normalized)
