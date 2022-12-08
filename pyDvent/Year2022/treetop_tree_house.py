import numpy as np


def treetop_tree_house(input_path):
    with open(input_path, 'r') as input_file:
        grid = np.matrix(" ".join(input_file.read().rstrip()).replace('\n', ';'))
        inner_trees = list(filter(lambda iv: 0 < iv[0][0] < grid.shape[0] - 1 and 0 < iv[0][1] < grid.shape[1] - 1,
                             np.ndenumerate(grid)))

        def calculate_visibility(grid, row, column, tree):
            visibility = max(np.squeeze(np.asarray(grid[row]))[column + 1:]) < tree
            visibility = visibility or max(reversed(np.squeeze(np.asarray(grid[row]))[: column])) < tree
            visibility = visibility or max(reversed(np.squeeze(np.asarray(grid[:, column]))[0: row])) < tree
            visibility = visibility or max(np.squeeze(np.asarray(grid[:, column]))[row + 1:]) < tree
            return visibility

        def count_visible_trees(trees, height):
            return next((x[0] + 1 for x in enumerate(trees) if x[1] >= height), len(trees))

        def calculate_score(grid, row, column, tree):
            score = count_visible_trees(np.squeeze(np.asarray(grid[row]))[column + 1:], tree)  # Trees to the right
            score *= count_visible_trees(list(reversed(np.squeeze(np.asarray(grid[row]))[: column])), tree)  # Trees to the left
            score *= count_visible_trees(list(reversed(np.squeeze(np.asarray(grid[:, column]))[0: row])), tree)  # Trees above
            score *= count_visible_trees(np.squeeze(np.asarray(grid[:, column]))[row + 1:], tree)  # Trees below
            return score

        outer_visible = grid.shape[0] * 2 + grid.shape[1] * 2 - 4
        inner_visible = sum(calculate_visibility(grid, x[0][0], x[0][1], x[1]) for x in inner_trees)
        result2 = max(calculate_score(grid, x[0][0], x[0][1], x[1]) for x in inner_trees)

        return outer_visible + inner_visible, result2
