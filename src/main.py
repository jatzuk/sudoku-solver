import time

initial_field = [
    [5, 0, 0, 0, 0, 7, 0, 1, 0],
    [0, 4, 0, 0, 0, 0, 0, 0, 0],
    [1, 9, 0, 0, 0, 0, 0, 0, 0],

    [9, 0, 0, 0, 0, 0, 0, 4, 5],
    [0, 0, 0, 3, 0, 9, 0, 0, 6],
    [4, 0, 3, 0, 0, 6, 0, 0, 0],

    [7, 3, 0, 5, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 2, 0, 7, 9],
    [0, 1, 0, 0, 6, 0, 0, 0, 0]
]


class SudokuSolver:
    def __init__(self, field):
        self.field = field

    def is_valid(self, row: int, col: int, n: int) -> bool:
        for i in range(len(self.field)):
            if self.field[row][i] == n:
                # print("Row check: can not put value", n, "at", row, col)
                return False

        for i in range(len(self.field)):
            if self.field[i][col] == n:
                # print("Col check: can not put value", n, "at", row, col)
                return False

        squareRow = (row // 3) * 3
        squareCol = (col // 3) * 3
        for i in range(3):
            for j in range(3):
                if self.field[squareRow + i][squareCol + j] == n:
                    # print("Square check: can not put value", n, "at", row, col)
                    return False

        return True

    def solve(self) -> bool:
        empty_cell = self.find_empty()
        if not empty_cell:
            return True

        row, col = empty_cell
        for n in range(1, 10):
            if self.is_valid(row, col, n):
                self.field[row][col] = n
                if self.solve():
                    return True
                self.field[row][col] = 0

        return False

    def find_empty(self) -> [int]:
        for row in range(len(self.field)):
            for col in range(len(self.field[row])):
                if self.field[row][col] == 0:
                    return (row, col)
        return None

    def print_field(self):
        for row in range(len(self.field)):
            for col in range(len(self.field[row])):
                print(self.field[row][col], end=" ")
            print()
        print("-" * len(self.field) * 2)


def main():
    solver = SudokuSolver(initial_field)
    solver.print_field()
    start = time.process_time()
    solver.solve()
    print("time taken:{0:.4f}".format(time.process_time() - start))
    solver.print_field()


if __name__ == "__main__":
    main()
