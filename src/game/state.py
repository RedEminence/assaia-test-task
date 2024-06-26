from typing import Union

from game.board import GameBoard


class GameState:
    def __init__(
            self,
            board: GameBoard,
            players: list[Union[int, str]],
            points_to_win: int = 4,
    ):
        if not players or len(players) < 2:
            raise ValueError("Not a valid player list.")

        if points_to_win < 1:
            raise Exception("points_to_win must be greater than zero")

        self._points_to_win = points_to_win

        self._board = board
        self._players = players
        self._current_player_index = 0

    def get_current_player(self):
        return self._players[self._current_player_index]

    def display_current_state(self):
        self._board.display_board()

    def make_turn(self, column: int):
        self._board.update_board(column, self.get_current_player())

    def switch_player(self):
        if self._current_player_index < len(self._players) - 1:
            self._current_player_index += 1
        else:
            self._current_player_index = 0

    def check_for_winner(self) -> bool:
        board = self._board.get_grid()
        for column in range(self._board.columns):
            for row in range(self._board.rows):
                if board[row][column] == self.get_current_player():
                    if any([
                        self._check_for_win_vertically(row, column),
                        self._check_for_win_horizontally(row, column),
                        self._check_for_win_diagonally(row, column)
                    ]):
                        return True

        return False

    def _check_for_win_horizontally(self, row: int, column: int) -> bool:
        count = 0
        for c in range(column, min(column + self._points_to_win, self._board.columns)):
            if self._board.get_grid()[row][c] == self.get_current_player():
                count += 1
            else:
                break

        return count >= self._points_to_win

    def _check_for_win_vertically(self, row: int, column: int) -> bool:
        count = 0
        for r in range(row, min(row + self._points_to_win, self._board.rows)):
            if self._board.get_grid()[r][column] == self.get_current_player():
                count += 1
            else:
                break

        return count >= self._points_to_win

    def _check_for_win_diagonally(self, row: int, column: int) -> bool:
        return (self._check_slope(row, column, 1, 1)
                or self._check_slope(row, column, 1, -1))

    def _check_slope(
            self,
            row: int,
            column: int,
            row_increment: int,
            column_increment: int
    ) -> bool:
        count = 1

        r, c = row + row_increment, column + column_increment

        while 0 <= r < self._board.rows and 0 <= c < self._board.columns:
            if self._board.get_grid()[r][c] == self.get_current_player():
                count += 1
                if count >= self._points_to_win:
                    return True
            else:
                break

            r += row_increment
            c += column_increment

        return False
