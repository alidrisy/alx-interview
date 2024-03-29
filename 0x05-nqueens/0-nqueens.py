#!/usr/bin/python3
""" Model The N queens puzzle is the challenge of
placing N non-attacking queens """
import sys


def is_safe(grid, y, x, n):
    """test wither its safe or not"""

    for i in range(n):
        if grid[y][i] == 1:
            return False
        if grid[i][x] == 1:
            return False
        if i + y < n and i + x < n:
            if grid[y+i][x+i] == 1:
                return False
        if y - i >= 0 and x - i >= 0:
            if grid[y-i][x-i] == 1:
                return False

        if y - i >= 0 and x + i < n:
            if grid[y-i][x+i] == 1:
                return False

        if y + i < n and x - i >= 0:
            if grid[y+i][x-i] == 1:
                return False
    return True


def print_grid(grid, n):
    """ Print the solution """
    solution = []
    for y in range(n):
        for x in range(n):
            if grid[y][x] == 1:
                solution.append([y, x])
    print(solution)


def solve(grid, y, n):
    """ Placing N non-attacking queens on an N×N chessboard. """
    if y == n:
        print_grid(grid, n)
        return

    for x in range(n):
        if grid[y][x] == 0:
            if is_safe(grid, y, x, n):
                grid[y][x] = 1
                solve(grid, y + 1, n)
                grid[y][x] = 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except Exception:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    grid = [[0] * n for i in range(n)]
    solve(grid, 0, n)
