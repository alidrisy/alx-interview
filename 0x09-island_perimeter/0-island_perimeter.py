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
                y += 1
    return (int(y / 2) + 1) * 4
