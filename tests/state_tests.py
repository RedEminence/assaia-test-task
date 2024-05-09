import unittest

from game.board import GameBoard
from game.state import GameState


class GameTests(unittest.TestCase):
    def setUp(self):
        board = GameBoard(3, 3)
        self._test_state = GameState(board, [1, 2], 3)

    def test_switch_player_ok(self):
        self.assertEqual(self._test_state.get_current_player(), 1)
        self._test_state.switch_player()
        self.assertEqual(self._test_state.get_current_player(), 2)

    def test_check_diagonal_win_condition_ok(self):
        self._test_state._board._grid = (
            [1, None, None],
            [None, 1, None],
            [None, None, 1]
        )
        self.assertTrue(self._test_state._check_for_win_diagonally(0, 0))

        self._test_state._board._grid = (
            [None, None, 1],
            [None, 1, None],
            [1, None, None]
        )

        self.assertTrue(self._test_state._check_for_win_diagonally(0, 2))

    def test_check_diagonal_win_condition_fail(self):
        self._test_state._board._grid = (
            [1, None, None],
            [None, 2, None],
            [None, None, 1]
        )
        self.assertFalse(self._test_state._check_for_win_diagonally(0, 0))

        self._test_state._board._grid = (
            [None, None, None],
            [None, None, None],
            [1, None, None]
        )

        self.assertFalse(self._test_state._check_for_win_diagonally(0, 2))

    def test_check_horizontal_win_condition_ok(self):
        self._test_state._board._grid = (
            [1, 1, 1],
            [None, 1, None],
            [None, None, None]
        )
        self.assertTrue(self._test_state._check_for_win_horizontally(0, 0))

        self._test_state._board._grid = (
            [None, None, 1],
            [1, 1, 1],
            [1, None, None]
        )

        self.assertTrue(self._test_state._check_for_win_horizontally(1, 0))

    def test_check_horizontal_win_condition_fail(self):
        self._test_state._board._grid = (
            [1, 2, None],
            [None, None, None],
            [None, None, 1]
        )
        self.assertFalse(self._test_state._check_for_win_horizontally(0, 0))

        self._test_state._board._grid = (
            [None, None, None],
            [None, None, None],
            [1, 2, 2]
        )

        self.assertFalse(self._test_state._check_for_win_horizontally(0, 2))


    def test_check_vertical_win_condition_ok(self):
        self._test_state._board._grid = (
            [1, 2, 2],
            [1, 1, None],
            [1, None, None]
        )
        self.assertTrue(self._test_state._check_for_win_vertically(0, 0))

        self._test_state._board._grid = (
            [2, 1, 1],
            [1, 2, 1],
            [1, 2, 1]
        )

        self.assertTrue(self._test_state._check_for_win_vertically(0, 2))

    def test_check_vertical_win_condition_fail(self):
        self._test_state._board._grid = (
            [1, 2, None],
            [None, None, None],
            [None, None, 1]
        )
        self.assertFalse(self._test_state._check_for_win_vertically(0, 0))

        self._test_state._board._grid = (
            [None, 1, None],
            [None, 2, None],
            [1, 2, 2]
        )

        self.assertFalse(self._test_state._check_for_win_vertically(0, 2))