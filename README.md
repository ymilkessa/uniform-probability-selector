# Uniform Probability Selector

This repo demonstrates a mechanism for selecting a leaf node from a tree while ensuring that all leaf nodes have
equal probability of being selected. In this context a leaf node is selected by starting from the root node and
picking branches at random until a leaf node is reached.

We can guarantee that all leafs have equal likelihood
of selection by simply making a _weighted_ random selection. The weight of a branch is proportional to the number of leaf nodes
beneath it.

## Example

I've included a program that uses a tree structure to select random locations on a square. The example provided
in `main.py` uses a square with 9 partitions as shown below.

<img src="https://github.com/ymilkessa/uniform-probability-selector/blob/main/demo_square_mapping.png" width=250>

The randomized point selectors for the partitions are arranged according to the following graph. Each leaf node can randomly select a point in its own domain.

<img src="https://github.com/ymilkessa/uniform-probability-selector/blob/main/demo_tree.png" width=400>

In the program, the root node is invoked to generate 500 points selected at random. In the default implementation, about half of the randomly selected points would be in section A. That is because if you pick a branch at random from the root, you should land on A about half of the time. Similarly, section B would have about one-fourth of these points, section C would have one-eighths, .... Blow is a plot of the resulting points on the square.

<img src="https://github.com/ymilkessa/uniform-probability-selector/blob/main/default_random_selections_display.gif" width=400>

However, when using the weighted branch selection (which I call normalized selection in the code), the same tree structure generates points as displayed below. This balanced distribution results because each leaf node in the tree has equal likelihood of being invoked.

<img src="https://github.com/ymilkessa/uniform-probability-selector/blob/main/normalized_selections_display.gif" width=400>

## How to Run the Demo

Here is how you can run the random point selectors.

Prerequisites: python3 and pipenv

Download the repo and run the following commands in the main folder.

To select points using the random branch selector, run:

```
pipenv run python .\main.py
```

In order to use the normalized probability selector, just add a `-n` to the command:

```
pipenv run python .\main.py -n
```
