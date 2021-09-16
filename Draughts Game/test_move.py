from move import Move
from piece import Piece

COLORS = ('black', 'DarkRed')
DIRECTIONS = ('left', 'right', 'left_king', 'right_king')

def test_new_click_within_valid_squares_noncapture_move():
    move = Move()
    piece = Piece(-25, -75, 'black')
    move.current_piece = piece
    move.valid_moveto_squares = ['left']
    assert(move.new_click_within_valid_squares_noncapture_move(-75, -25))
    assert(not move.new_click_within_valid_squares_noncapture_move(-25, -75))

    move.valid_moveto_squares = ['right']
    assert(move.new_click_within_valid_squares_noncapture_move(25, -25))
    assert(not move.new_click_within_valid_squares_noncapture_move(-25, -75))

    move.valid_moveto_squares = ['left_king']
    assert(move.new_click_within_valid_squares_noncapture_move(-75, -125))
    assert(not move.new_click_within_valid_squares_noncapture_move(-25, -75))

    move.valid_moveto_squares = ['right_king']
    assert(move.new_click_within_valid_squares_noncapture_move(25, -125))
    assert(not move.new_click_within_valid_squares_noncapture_move(-75, -125))

    move.valid_moveto_squares = ['left', 'right_king']
    assert(move.new_click_within_valid_squares_noncapture_move(25, -125))
    assert(move.new_click_within_valid_squares_noncapture_move(-75, -25))
    assert(not move.new_click_within_valid_squares_noncapture_move(-75, -125))
    assert(not move.new_click_within_valid_squares_noncapture_move(-25, -75))


def test__new_click_within_left_valid_square_noncapture_move():
    move = Move()
    piece = Piece(-25, -75, 'black')
    move.current_piece = piece
    assert(not move._new_click_within_left_valid_square_noncapture_move(-25, -75))
    assert(not move._new_click_within_left_valid_square_noncapture_move(25, -25))
    assert(move._new_click_within_left_valid_square_noncapture_move(-75, -25))


def test__new_click_within_right_valid_square_noncapture_move():
    move = Move()
    piece = Piece(-25, -75, 'black')
    move.current_piece = piece
    assert(not move._new_click_within_right_valid_square_noncapture_move(-25, -75))
    assert(move._new_click_within_right_valid_square_noncapture_move(25, -25))
    assert(not move._new_click_within_right_valid_square_noncapture_move(-75, -25))


def test__new_click_within_left_king_valid_square_noncapture_move():
    move = Move()
    piece = Piece(-25, -75, 'black')
    move.current_piece = piece
    assert(not move._new_click_within_left_king_valid_square_noncapture_move(-25, -125))
    assert(move._new_click_within_left_king_valid_square_noncapture_move(-75, -125))
    assert(not move._new_click_within_left_king_valid_square_noncapture_move(-75, -25))


def test__new_click_within_right_king_valid_square_noncapture_move():
    move = Move()
    piece = Piece(-25, -75, 'black')
    move.current_piece = piece
    assert(not move._new_click_within_right_king_valid_square_noncapture_move(-75, -125))
    assert(not move._new_click_within_right_king_valid_square_noncapture_move(25, -25))
    assert(move._new_click_within_right_king_valid_square_noncapture_move(25, -125))

def test_new_click_within_valid_squares_capture_move():
    move = Move()
    piece = Piece(-25, -75, 'black')
    move.current_piece = piece
    move.valid_moveto_squares = ['left']
    assert(move.new_click_within_valid_squares_capture_move(-125, 25))
    assert(not move.new_click_within_valid_squares_capture_move(75, 25))

    move.valid_moveto_squares = ['right']
    assert(move.new_click_within_valid_squares_capture_move(75, 25))
    assert(not move.new_click_within_valid_squares_capture_move(-125, 25))

    move.valid_moveto_squares = ['left_king']
    assert(move.new_click_within_valid_squares_capture_move(-125, -175))
    assert(not move.new_click_within_valid_squares_capture_move(75, -175))

    move.valid_moveto_squares = ['right_king']
    assert(move.new_click_within_valid_squares_capture_move(75, -175))
    assert(not move.new_click_within_valid_squares_capture_move(-125, -175))

    move.valid_moveto_squares = ['left', 'right_king']
    assert(move.new_click_within_valid_squares_capture_move(-125, 25))
    assert(move.new_click_within_valid_squares_capture_move(75, -175))
    assert(not move.new_click_within_valid_squares_capture_move(-75, -125))
    assert(not move.new_click_within_valid_squares_capture_move(75, 25))



def test__new_click_within_left_valid_square_capture_move():
    move = Move()
    piece = Piece(-25, -75, 'black')
    move.current_piece = piece
    assert(move._new_click_within_left_valid_square_capture_move(-125, 25))
    assert(not move._new_click_within_left_valid_square_capture_move(75, 25))
    assert(not move._new_click_within_left_valid_square_capture_move(-25, -75))


def test__new_click_within_right_valid_square_capture_move():
    move = Move()
    piece = Piece(-25, -75, 'black')
    move.current_piece = piece
    assert(move._new_click_within_right_valid_square_capture_move(75, 25))
    assert(not move._new_click_within_right_valid_square_capture_move(-125, 25))
    assert(not move._new_click_within_right_valid_square_capture_move(-25, -75))


def test__new_click_within_left_king_valid_square_capture_move():
    move = Move()
    piece = Piece(-25, -75, 'black')
    move.current_piece = piece
    assert(move._new_click_within_left_king_valid_square_capture_move(-125, -175))
    assert(not move._new_click_within_left_king_valid_square_capture_move(75, -175))
    assert(not move._new_click_within_left_king_valid_square_capture_move(-25, -75))


def test__new_click_within_right_king_valid_square_capture_move():
    move = Move()
    piece = Piece(-25, -75, 'black')
    move.current_piece = piece
    assert(move._new_click_within_right_king_valid_square_capture_move(75, -175))
    assert(not move._new_click_within_right_king_valid_square_capture_move(-125, -175))
    assert(not move._new_click_within_right_king_valid_square_capture_move(-25, -75))


