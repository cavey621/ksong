
from gamestate import GameState
from piece import Piece

COLORS = ('black', 'DarkRed')

def test_get_pieces():
    game = GameState()
    assert(game.get_pieces(COLORS[0])[0] == Piece(-125, -175, COLORS[0]))
    assert(game.get_pieces(COLORS[0])[11] == Piece(175, -75, COLORS[0]))
    assert(game.get_pieces(COLORS[1])[0] == Piece(-175, 75, COLORS[1]))


def test_exists_piece():
    game = GameState()
    assert(game.exists_piece(-125, -175))
    assert(game.exists_piece(-175, 75))
    assert(not game.exists_piece(-175, 25))


def test_get_piece():
    game = GameState()
    assert(game.get_piece(-25, -75) == Piece(-25, -75, COLORS[0]))
    assert(game.get_piece(-40, -60) == None)
    assert(game.get_piece(25, 75) == Piece(25, 75, COLORS[1]))
    assert(game.get_piece(175, 75) == None)


def test_move_piece():
    game = GameState()
    assert(game.get_piece(-25, -75) == Piece(-25, -75, COLORS[0]))
    assert(game.get_piece(-75, -25) == None)
    piece = Piece(-25, -75, COLORS[0])
    game.move_piece(piece, -75, -25)
    assert(game.get_piece(-25, -75) == None)
    assert(game.get_piece(-75, -25) == Piece(-75, -25, COLORS[0]))


def test_remove_piece():
    game = GameState()
    piece1 = Piece(-25, -75, COLORS[0])
    assert(len(game.black_pieces) + len(game.red_pieces) == 24)
    game.remove_piece(piece1)
    assert(len(game.black_pieces) + len(game.red_pieces) == 23)
    piece2 = Piece(25, 75, COLORS[1])
    game.remove_piece(piece2)
    assert(len(game.black_pieces) + len(game.red_pieces) == 22)
