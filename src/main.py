from game.board import GameBoard
from game.exceptions import GameException
from game.state import GameState


def run(
        players: list = None,
        rows: int = 6,
        columns: int = 7,
        points_to_win: int = 4,
):
    if not players:
        players = [1, 2]

    board = GameBoard(rows=rows, columns=columns)
    state = GameState(board=board, players=players, points_to_win=points_to_win)

    print('Starting the game, to quit type exit')
    state.display_current_state()

    while True:
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
            continue

        state.display_current_state()

        is_player_winner = state.check_for_winner()
        if is_player_winner:
            print(f"Player {current_player} wins!")
            return

        state.switch_player()

if __name__ == "__main__":
    run()
