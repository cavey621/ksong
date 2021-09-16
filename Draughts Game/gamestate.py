
from piece import Piece

class GameState:
    '''
        Class -- GameState
            Represents game state.
        Attributes:
            black_pieces -- a list of black pieces that are currently still
                in the game.
            red_pieces -- a list of red pieces that are currently still in 
                the game.
            turn_counts -- the number of turns so far in the game.
            game_over -- a boolean stating if the winner has been determined.
        Methods:
            get_pieces -- helper method to create a list of pieces
                for a color.
            exists_piece -- checks if the input x, y within a square that
                contains this piece.
            get_piece -- get the Piece object in a position.
            move_piece -- move the Piece piece to a position.
            remove_piece -- remove the piece from the game.
        '''

    COLORS = ('black', 'DarkRed')
    

    def __init__(self):
        '''
            Constructor -- creates a new instance of Gamestate
            Parameters:
                self -- creates a new instance of Gamestate
        '''
        self.black_pieces = self.get_pieces(self.COLORS[0])
        self.red_pieces = self.get_pieces(self.COLORS[1])
        self.turn_counts = 1
        self.game_over = False
        

    def get_pieces(self, color):
        '''
            Method -- get_pieces
                helper method to create a list of pieces for a color.
            Parameters:
                self -- the current Gamestate object
                color -- the color of pieces that is to be created
            Returns:
                the list of pieces in input color
        '''
        SQUARE = 50
        NUM_ROWS = 3
        NUM_COLS = 4
        pieces = []
        for row in range(NUM_ROWS):
            y = -SQUARE * 3.5 + SQUARE * row + \
                SQUARE * 5 * self.COLORS.index(color)
            for col in range(NUM_COLS):
                x = -SQUARE * 2.5 - SQUARE * self.COLORS.index(color) + \
                    SQUARE * 2 * col - SQUARE * (row % 2) \
                        * -self.COLORS.index(color)
                if color == self.COLORS[0] and row == 1:
                    x -= SQUARE
                pieces.append(Piece(x, y, color))
        return pieces


    def exists_piece(self, x, y):
        '''
            Method -- exists_piece
                checks if the input x, y within a square that contains
                this piece
            Parameters:
                self -- the current Piece object
                x -- the x coordinate of the position that is to be checked
                    for piece existence
                y -- the y coordinate of the position that is to be checked
                    for piece existence
            Returns:
                True if the position exists a piece, or False if not.
        '''
        for piece in self.black_pieces:
            if piece.exists_piece(x, y):
                return True
        for piece in self.red_pieces:
            if piece.exists_piece(x, y):
                return True
        return False


    def get_piece(self, x, y):
        '''
            Method -- get_piece
                get the Piece object in the position (x, y)
            Parameters:
                self -- the current Gamestate object
                x -- the x coordinate of the position that will be 
                    getting the piece from.
                y -- the y coordinate of the position that will be 
                    getting the piece from.
            Returns:
                the Piece in the position (x, y) if there exists
                a piece, otherwise None.
        '''
        if self.exists_piece(x, y):
            for black_piece in self.black_pieces:
                if black_piece.x == x and black_piece.y == y:
                    return black_piece
            for red_piece in self.red_pieces:
                if red_piece.x == x and red_piece.y == y:
                    return red_piece
        return None


    def move_piece(self, piece, to_x, to_y):
        '''
            Method -- move_piece
                move the Piece piece to the position (to_x, to_y).
            Parameters:
                self -- the current Gamestate object
                piece -- the Piece that is to be moved.
                to_x -- the x coordinate of the position that the
                    Piece piece will be moved to.
                to_y -- the y coordinate of the position that the
                    Piece piece will be moved to.
        '''
        for p in self.black_pieces:
            if p == piece:
                p.x = to_x
                p.y = to_y
        for p in self.red_pieces:
            if p == piece:
                p.x = to_x
                p.y = to_y
    

    def remove_piece(self, piece):
        '''
            Method -- remove_piece
                remove the piece from the game.
            Parameters:
                self -- the current Gamestate object
                piece -- the Piece that is to be removed.
        '''
        for piece_set in (self.black_pieces, self.red_pieces):
            if piece in piece_set:
                piece_set.remove(piece)
