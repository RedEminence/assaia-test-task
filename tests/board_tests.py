import unittest

from game.board import GameBoard
from game.exceptions import GameException


class BoardTests(unittest.TestCase):
    def test_create_board_ok(self):
        board = GameBoard(2, 2)
        self.assertEqual(board.get_grid(), [[None, None], [None, None]])

    def test_create_board_invalid_arguments_fail(self):
        self.assertRaises(
            GameException, GameBoard, None, None
        )
        self.assertRaises(GameException, GameBoard, -1, 7)

    def test_update_board_ok(self):
        board = GameBoard(2, 2)
        board.update_board(0, 1)
        self.assertEqual(board.get_grid(), [[1, None], [None, None]])

    def test_update_board_invalid_arguments_fail(self):
        board = GameBoard(2, 2)
        self.assertRaises(GameException, board.update_board, 6, 1)