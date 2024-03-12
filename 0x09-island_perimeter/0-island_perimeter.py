#!/usr/bin/python3
"""
Model for island_perimeter function
"""


def island_perimeter(grid):
    """Returns the perimeter of the island described in grid"""
    y = 0
    for i in range(len(grid)):
        for x in range(len(grid[i])):
            if grid[i][x] == 1:
                y += 4
                if i > 0 and grid[i - 1][x] == 1:
                    y -= 2
                if x > 0 and grid[i][x - 1] == 1:
                    y -= 2
                print(y)
    return y
