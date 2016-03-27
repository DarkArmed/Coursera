"""
Mini-max Tic-Tac-Toe Player
"""

import poc_ttt_gui
import poc_ttt_provided as provided

# Set timeout, as mini-max can take a long time
import codeskulptor
codeskulptor.set_timeout(60)

# SCORING VALUES - DO NOT MODIFY
SCORES = {provided.PLAYERX: 1,
          provided.DRAW: 0,
          provided.PLAYERO: -1}

def mm_move(board, player):
    """
    Make a move on the board.
    
    Returns a tuple with two elements.  The first element is the score
    of the given board and the second element is the desired move as a
    tuple, (row, col).
    """
    state = board.check_win()
    if state != None:
        return SCORES[state], (-1, -1)
    minimax_score = -2
    minimax_move = None

    for move in board.get_empty_squares():
        current_board = board.clone()
        current_board.move(move[0], move[1], player)
        score = mm_move(current_board, provided.switch_player(player))[0]
        if score == SCORES[player]:
            return score, move
        elif score * SCORES[player] > minimax_score:
            minimax_score = score * SCORES[player]
            minimax_move = move
    return minimax_score * SCORES[player], minimax_move

def move_wrapper(board, player, trials):
    """
    Wrapper to allow the use of the same infrastructure that was used
    for Monte Carlo Tic-Tac-Toe.
    """
    move = mm_move(board, player)
    assert move[1] != (-1, -1), "returned illegal move (-1, -1)"
    return move[1]

# Test game with the console or the GUI.
# Uncomment whichever you prefer.
# Both should be commented out when you submit for
# testing to save time.

# provided.play_game(move_wrapper, 1, False)
# poc_ttt_gui.run_gui(3, provided.PLAYERX, move_wrapper, 1, False)
