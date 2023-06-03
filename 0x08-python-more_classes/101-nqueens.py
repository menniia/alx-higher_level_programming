#!/usr/bin/python3

import sys

class NQueens:
    def __init__(self, n):
        self.n = n
        self.solutions = []

    def solve(self):
        queens = [-1] * self.n
        self.place_queens(queens, 0)
        return self.solutions

    def place_queens(self, queens, row):
        if row == self.n:
            solution = [[i, queens[i]] for i in range(self.n)]
            self.solutions.append(solution)
        else:
            for col in range(self.n):
                if self.is_valid_placement(queens, row, col):
                    queens[row] = col
                    self.place_queens(queens, row + 1)

    def is_valid_placement(self, queens, row, col):
        for i in range(row):
            if (
                queens[i] == col or
                queens[i] - col == i - row or
                queens[i] - col == row - i
            ):
                return False
        return True

def print_solutions(solutions):
    for solution in solutions:
        print(solution)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
        if n < 4:
            raise ValueError
    except ValueError:
        print("N must be a number greater or equal to 4")
        sys.exit(1)

    n_queens = NQueens(n)
    solutions = n_queens.solve()
    print_solutions(solutions)

