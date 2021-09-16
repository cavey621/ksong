from piece import Piece

def test_exists_piece():
    piece = Piece(-25, -75, 'black')
    assert(piece.exists_piece(-25, -75))
    assert(piece.exists_piece(-45, -51))
    assert(not piece.exists_piece(-51, -101))
    assert(not piece.exists_piece(1, -51))

    
def test_eq():
    piece1 = Piece(-25, -75, 'black')
    piece2 = Piece(-25, -75, 'red')
    assert(piece1 != piece2)
    piece3 = Piece(-25, -75, 'black')
    assert(piece1 == piece3)

def test_str():
    piece1 = Piece(-25, -75, 'black')
    assert(str(piece1) == 'This piece is in black, located at (-25, -75).')
    piece2 = Piece(-25, -75, 'red')
    assert(str(piece2) == 'This piece is in red, located at (-25, -75).')
