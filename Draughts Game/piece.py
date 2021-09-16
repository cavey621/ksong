
class Piece:
    '''
        Class - Piece
            Represents a piece
        Attributes:
            x -- the x location of the piece
            y -- the y location of the piece
            color -- the color of the piece
            is_king -- equals to True if the piece is king, otherwise False
        Methods:
            exists_piece -- checks if the input x, y within a square that
            contains this piece.
    '''
    SQUARE = 50

    def __init__(self, x, y, color):
        '''
            Constructor -- creates a new instance of Piece
            Parameters:
                self -- the current Piece object
                x -- the x location of the piece
                y -- the y location of the piece
                color -- the color of the piece
        '''
        self.x = x  # (x, y) middle of the square
        self.y = y
        self.color = color # "black" or "DarkRed"
        self.is_king = False
    

    def exists_piece(self, x, y): 
        '''
            Method -- exists_piece
                checks if the input x, y within a square that contains this piece
            Parameters:
                self -- the current Piece object
                x -- the x coordinate of the position that is to be checked for
                piece existence
                y -- the y coordinate of the position that is to be checked for
                piece existence
            Returns:
                True if the position exists a piece, or False if not.
        '''
        # check if the input x, y within a square that contains this piece
        return x > self.x - self.SQUARE / 2 and x < self.x + self.SQUARE / 2 \
            and y > self.y - self.SQUARE / 2 and y < self.y + self.SQUARE / 2


    def __eq__(self, piece2):  
        '''
            Method -- __eq__
                Checks if two Piece objects are equal
            Parameters:
                self -- The current Piece object
                other -- An object to compare self to.
            Returns:
                True if the two objects are equal, False otherwise.
        '''
        return self.x == piece2.x and self.y == piece2.y and \
            self.color == piece2.color


    def __str__(self):
        '''
            Method -- __str__
                Creates a string representation of the Piece
            Parameter:
                self -- The current Piece object
            Returns:
                A string representation of the Piece.
        '''
        return "This piece is in {}, located at ({}, {})."\
            .format(self.color, self.x, self.y)
