"""
Monte Carlo Tic-Tac-Toe Player
"""

import random
import poc_ttt_gui
import poc_ttt_provided as provided

# Constants for Monte Carlo simulator
# You may change the values of these constants as desired, but
#  do not change their names.
NTRIALS = 500       # Number of trials to run
SCORE_CURRENT = 1.0 # Score for squares played by the current player
SCORE_OTHER = 1.0   # Score for squares played by the other player
    
# Add your functions here.
def mc_trial(board, player):
    """
    Make random moves until the game is over,
    alternating between players.
    """
    square = random.choice(board.get_empty_squares())
    board.move(square[0], square[1], player)
    if board.check_win() == None:
        mc_trial(board, provided.switch_player(player))
        
def mc_update_scores(scores, board, player):
    """
    Update the scores for current player.
    """
    if board.check_win() == provided.DRAW:
        return
    sig = 1 if board.check_win() == player else -1
    for row in range(board.get_dim()):
        for col in range(board.get_dim()):
            if board.square(row, col) == player:
                scores[row][col] += sig * SCORE_CURRENT
            elif board.square(row, col) == provided.switch_player(player):
                scores[row][col] -= sig * SCORE_OTHER
    
def get_best_move(board, scores):
    """
    Find all the empty squares with the maximum score and 
    randomly return one of them as a (row, column) tuple. 
    """
    best_moves = []
    max_score = -10000
    for row in range(board.get_dim()):
        for col in range(board.get_dim()):
            if board.square(row, col) != provided.EMPTY or scores[row][col] < max_score:
                continue
            if scores[row][col] > max_score:
                best_moves = [(row, col)]
                max_score = scores[row][col]
            elif scores[row][col] == max_score:
                best_moves.append((row, col))
    return random.choice(best_moves)

def mc_move(board, player, trials):
    """
    Run several trials as Monte Carlo simulation.
    Return a move with maximum score in the form of a (row, col) tuple.
    """
    scores = [[0] * board.get_dim() for dummy_i in range(board.get_dim())]
    for dummy_i in range(trials):
        board_trial = board.clone()
        mc_trial(board_trial, player)
        mc_update_scores(scores, board_trial, player)
    return get_best_move(board, scores)


# Test game with the console or the GUI.  Uncomment whichever 
# you prefer.  Both should be commented out when you submit 
# for testing to save time.

# provided.play_game(mc_move, NTRIALS, False)
# poc_ttt_gui.run_gui(3, provided.PLAYERX, mc_move, NTRIALS, False)
