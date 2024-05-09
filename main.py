from game.board import GameBoard
from game.exceptions import GameException
from game.state import GameState


def run(
        players: list = None,
        rows: int = 6,
        columns: int = 7,
        points_for_win: int = 4,
):
    if not players:
        players = [1, 2]

    board = GameBoard(rows=rows, columns=columns)
    state = GameState(board=board, players=players, points_for_win=points_for_win)

    print('Starting the game, to quit type exit')

    while True:
        state.display_current_state()
        current_player = state.get_current_player()
        player_input = input(f"Turn for player {current_player}. Enter column index: ")

        if player_input == 'exit':
            return

        try:
            player_input = int(player_input)
        except ValueError:
            print("Player input is not a valid integer")
            continue

        try:
            state.make_turn(player_input)
        except GameException as ex:
            print(f"Could not update board: {ex}. Try again please")

        is_player_winner = state.check_for_winner()

        if is_player_winner:
            print(f"Player {current_player} wins!")
            return

        state.switch_player()

if __name__ == "__main__":
    run()
