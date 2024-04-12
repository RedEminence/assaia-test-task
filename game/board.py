from typing import Optional

from game.exceptions import GameException


class GameBoard:
    def __init__(self, rows: int = 6, columns: int = 7):
        if not rows or not columns:
            raise Exception("y and x must be set")

        if rows < 1 or columns < 1:
            raise Exception("x and y must be greater than zero")

        self.rows = rows
        self.columns = columns
        self._grid = [[None for _ in range(columns)] for _ in range(rows)]

    def get_grid(self) -> list[list[Optional[str]]]:
        return self._grid

    def update_board(self, column: int, player_number: int) -> None:
        if column < 0 or column > self.columns - 1:
            raise GameException("Invalid coordinate for column")

        for row in range(self.columns):
            if self._grid[row][column] is None:
                self._grid[row][column] = player_number
                return

        raise GameException("The column is already fully occupied")

    def display_board(self) -> None:
        for row in reversed(self._grid):
            print("|", end="")
            for cell in row:
                if cell is None:
                    print("   |", end="")
                else:
                    print(f" {cell} |", end="")
            print("\n" + "-" * (self.columns * 4 + 1))
