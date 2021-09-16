
from main import is_red_turn, king_moves_backwards, is_valid_position, \
    get_mid_point_of_square, get_left_btm_point_of_square, get_multiple_square
from move import Move
from gamestate import GameState
from piece import Piece

PIECE_COLORS = ("DarkRed", "black")

def test_is_red_turn():
    assert(not is_red_turn(PIECE_COLORS[1]))
    assert(is_red_turn(PIECE_COLORS[0]))


def test_king_moves_backwards():
    move = Move()
    piece = Piece(-25, -75, 'black')
    piece.is_king = True
    move.current_piece = piece
    assert(king_moves_backwards(piece, -125))
    assert(not king_moves_backwards(piece, 125))

def test_is_valid_position():
    assert(is_valid_position(-25, -75))
    assert(is_valid_position(125, 195))
    assert(is_valid_position(0, 0))
    assert(is_valid_position(199, -199))
    assert(not is_valid_position(-201, 0))
    assert(not is_valid_position(0, 202))
    assert(not is_valid_position(-200, 202))


def test_get_mid_point_of_square():
    assert(get_mid_point_of_square(102) == 125)
    assert(get_mid_point_of_square(0) == -25)
    assert(get_mid_point_of_square(28) == 25)
    assert(get_mid_point_of_square(-72) == -75)
    assert(get_mid_point_of_square(-162) == -175)
    assert(not get_mid_point_of_square(-162) == -162)
    assert(not get_mid_point_of_square(78) == 78)

def test_get_left_btm_point_of_square():
    assert(get_left_btm_point_of_square(25) == 0)
    assert(get_left_btm_point_of_square(-125) == -150)
    assert(get_left_btm_point_of_square(-113) == -150)
    assert(not get_left_btm_point_of_square(-113) == -113)
    assert(not get_left_btm_point_of_square(25) == 25)


def test_get_multiple_square():
    assert(get_multiple_square(150) == 2)
    assert(get_multiple_square(175) == 3)
    assert(get_multiple_square(55) == 1)
    assert(get_multiple_square(49) == 0)
    assert(not get_multiple_square(55) == 0)
    assert(not get_multiple_square(155) == 4)