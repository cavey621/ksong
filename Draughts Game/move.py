
from piece import Piece

class Move:
    '''
        Class -- Move
            Represents a move.
        Attributes:
            is_move -- determines if this is in a move state.
            is_non_capture_moving -- determines if this is in non-capture
                move state.
            current_piece -- the current moving piece, a Piece object.
            valid_moveto_squares -- a list of valid potential squares 
                moving to.
            second_next_left_square_is_added -- determines if the second 
                next left square has been added to the list.
            continue_capture_move -- determines if the move is continued 
                implementing.
        Methods:
            new_click_within_valid_squares_noncapture_move -- checks if 
                the new click is within valid squares for a non-capture move.
            _new_click_within_left_valid_square_noncapture_move -- helper 
                method checks if the new click is within left valid squares
                for a non-capture move.
            _new_click_within_right_valid_square_noncapture_move -- helper 
                method checks if the new click is within right valid squares
                for a non-capture move.
            _new_click_within_left_king_valid_square_noncapture_move -- 
                helper method checks if the new click on a king piece is 
                within left valid squares for a non-capture move.
            _new_click_within_right_king_valid_square_noncapture_move -- 
                helper method checks if the new click on a king piece is
                within right valid squares for a non-capture move.
            new_click_within_valid_squares_capture_move -- 
                checks if the new click is within valid squares for a capture
                move.
            _new_click_within_left_valid_square_capture_move -- 
                helper method checks if the new click is within left valid
                squares for a capture move.
            _new_click_within_right_valid_square_capture_move -- 
                helper method checks if the new click is within right valid
                squares for a capture move.
            _new_click_within_left_king_valid_square_capture_move -- 
                helper method checks if the new click on a king piece is
                within left valid squares for a capture move.
            _new_click_within_right_king_valid_square_capture_move -- 
                helper method checks if the new click on a king piece is
                within right valid squares for a capture move.
    '''

    SQUARE = 50 # The size of each square in the checkerboard.
    PIECE_COLORS = ("DarkRed", "black")
    PIECE_COLORS_REVERSE = ("black", "DarkRed")
    MOVE_DIRECTIONS = ['left', 'right', 'left_king', 'right_king']


    def __init__(self):
        '''
            Constructor -- creates a new instance of Move
            Parameters:
                self -- creates a new instance of Move
        '''
        self.is_move = False
        self.is_non_capture_moving = False
        self.current_piece = None
        self.valid_moveto_squares = []
        self.second_next_left_square_is_added = False
        self.continue_capture_move = False


    def new_click_within_valid_squares_noncapture_move(self, x, y):
        '''
            Method -- new_click_within_valid_squares_noncapture_move
                checks if the new click is within valid squares for a
                non-capture move
            Parameters:
                self -- the current Move object
                x -- the x coordinate of the position that is to be checked
                y -- the y coordinate of the position that is to be checked
            Returns:
                True if the new click is within valid squares, or False 
                if not.
        '''
        valid_click = False
        for i in self.valid_moveto_squares:
            if i == self.MOVE_DIRECTIONS[0]:
                valid_click = valid_click or \
                    self._new_click_within_left_valid_square_noncapture_move(x, y)
            if i == self.MOVE_DIRECTIONS[1]:
                valid_click = valid_click or \
                    self._new_click_within_right_valid_square_noncapture_move(x, y)
            if i == self.MOVE_DIRECTIONS[2]:
                valid_click = valid_click or \
                    self._new_click_within_left_king_valid_square_noncapture_move(x, y)
            if i == self.MOVE_DIRECTIONS[3]:
                valid_click = valid_click or \
                    self._new_click_within_right_king_valid_square_noncapture_move(x, y)
        return valid_click

  
    def _new_click_within_left_valid_square_noncapture_move(self, x, y):
        '''
            Method -- _new_click_within_left_valid_square_noncapture_move
                helper method checks if the new click is within left valid
                squares for a non-capture move
            Parameters:
                self -- the current Move object
                x -- the x coordinate of the position that is to be checked
                y -- the y coordinate of the position that is to be checked
            Returns:
                True if the new click is within left valid squares, or False
                if not.
        '''
        return x > self.current_piece.x - self.SQUARE * 1.5 \
                and x < self.current_piece.x - self.SQUARE / 2 \
                and y < self.current_piece.y - self.SQUARE / 2 + self.SQUARE * 2 * \
                    self.PIECE_COLORS.index(self.current_piece.color) \
                and y > self.current_piece.y - self.SQUARE * 1.5 + self.SQUARE * 2 * \
                    self.PIECE_COLORS.index(self.current_piece.color)


    def _new_click_within_right_valid_square_noncapture_move(self, x, y):
        '''
            Method -- _new_click_within_right_valid_square_noncapture_move
                helper method checks if the new click is within right valid
                squares for a non-capture move
            Parameters:
                self -- the current Move object
                x -- the x coordinate of the position that is to be checked
                y -- the y coordinate of the position that is to be checked
            Returns:
                True if the new click is within right valid squares, or False
                if not.
        '''
        return x > self.current_piece.x + self.SQUARE / 2 \
                and x < self.current_piece.x + self.SQUARE * 1.5 \
                and y < self.current_piece.y - self.SQUARE / 2 + self.SQUARE * 2 * \
                    self.PIECE_COLORS.index(self.current_piece.color) \
                and y > self.current_piece.y - self.SQUARE * 1.5 + self.SQUARE * 2 * \
                    self.PIECE_COLORS.index(self.current_piece.color)


    def _new_click_within_left_king_valid_square_noncapture_move(self, x, y):
        '''
            Method -- _new_click_within_left_king_valid_square_noncapture_move
                helper method checks if the new click on a king piece is 
                within left valid squares for a non-capture move
            Parameters:
                self -- the current Move object
                x -- the x coordinate of the position that is to be checked
                y -- the y coordinate of the position that is to be checked
            Returns:
                True if the new click on a king piece is within left valid
                squares, or False if not.
        '''
        return x > self.current_piece.x - self.SQUARE * 1.5 \
                and x < self.current_piece.x - self.SQUARE / 2 \
                and y < self.current_piece.y - self.SQUARE / 2 + self.SQUARE * 2 * \
                    self.PIECE_COLORS_REVERSE.index(self.current_piece.color)\
                and y > self.current_piece.y - self.SQUARE * 1.5 + self.SQUARE * 2 * \
                    self.PIECE_COLORS_REVERSE.index(self.current_piece.color)


    def _new_click_within_right_king_valid_square_noncapture_move(self, x, y):
        '''
            Method -- _new_click_within_right_king_valid_square_noncapture_move
                helper method checks if the new click on a king piece is 
                within right valid squares for a non-capture move
            Parameters:
                self -- the current Move object
                x -- the x coordinate of the position that is to be checked
                y -- the y coordinate of the position that is to be checked
            Returns:
                True if the new click on a king piece is within right valid
                squares, or False if not.
        '''
        return x > self.current_piece.x + self.SQUARE / 2 \
                and x < self.current_piece.x + self.SQUARE * 1.5 \
                and y < self.current_piece.y - self.SQUARE / 2 + self.SQUARE * 2 * \
                    self.PIECE_COLORS_REVERSE.index(self.current_piece.color)\
                and y > self.current_piece.y - self.SQUARE * 1.5 + self.SQUARE * 2 * \
                    self.PIECE_COLORS_REVERSE.index(self.current_piece.color)


    def new_click_within_valid_squares_capture_move(self, x, y):
        '''
            Method -- new_click_within_valid_squares_capture_move
                checks if the new click is within valid squares for a capture
                move
            Parameters:
                self -- the current Move object
                x -- the x coordinate of the position that is to be checked
                y -- the y coordinate of the position that is to be checked
            Returns:
                True if the new click is within valid squares, or False if
                not.
        '''
        valid_click = False
        for i in self.valid_moveto_squares:
            if i == self.MOVE_DIRECTIONS[0]:
                valid_click = valid_click or \
                    self._new_click_within_left_valid_square_capture_move(x, y)
            if i == self.MOVE_DIRECTIONS[1]:
                valid_click = valid_click or \
                    self._new_click_within_right_valid_square_capture_move(x, y)
            if i == self.MOVE_DIRECTIONS[2]:
                valid_click = valid_click or \
                    self._new_click_within_left_king_valid_square_capture_move(x, y)
            if i == self.MOVE_DIRECTIONS[3]:
                valid_click = valid_click or \
                    self._new_click_within_right_king_valid_square_capture_move(x, y)
        return valid_click


    def _new_click_within_left_valid_square_capture_move(self, x, y):
        '''
            Method -- _new_click_within_left_valid_square_capture_move
                helper method checks if the new click is within left valid 
                squares for a capture move
            Parameters:
                self -- the current Move object
                x -- the x coordinate of the position that is to be checked
                y -- the y coordinate of the position that is to be checked
            Returns:
                True if the new click is within left valid squares, or False
                if not.
        '''
        return x > self.current_piece.x - self.SQUARE * 2.5 \
                and x < self.current_piece.x - self.SQUARE * 1.5 \
                and y < self.current_piece.y - self.SQUARE * 1.5 + self.SQUARE * 4 \
                     * self.PIECE_COLORS.index(self.current_piece.color) \
                and y > self.current_piece.y - self.SQUARE * 2.5 + self.SQUARE * 4 \
                    * self.PIECE_COLORS.index(self.current_piece.color)


    def _new_click_within_right_valid_square_capture_move(self, x, y):
        '''
            Method -- _new_click_within_right_valid_square_capture_move
                helper method checks if the new click is within right
                valid squares for a capture move
            Parameters:
                self -- the current Move object
                x -- the x coordinate of the position that is to be checked
                y -- the y coordinate of the position that is to be checked
            Returns:
                True if the new click is within right valid squares, or False
                if not.
        '''
        return x > self.current_piece.x + self.SQUARE * 1.5 \
                and x < self.current_piece.x + self.SQUARE * 2.5 \
                and y < self.current_piece.y - self.SQUARE * 1.5 + self.SQUARE * 4 \
                    * self.PIECE_COLORS.index(self.current_piece.color) \
                and y > self.current_piece.y - self.SQUARE * 2.5 + self.SQUARE * 4 \
                    * self.PIECE_COLORS.index(self.current_piece.color)


    def _new_click_within_left_king_valid_square_capture_move(self, x, y):
        '''
            Method -- _new_click_within_left_king_valid_square_capture_move
                helper method checks if the new click on a king piece is
                within left valid squares for a capture move
            Parameters:
                self -- the current Move object
                x -- the x coordinate of the position that is to be checked
                y -- the y coordinate of the position that is to be checked
            Returns:
                True if the new click on a king piece is within left valid 
                squares, or False if not.
        '''
        return x > self.current_piece.x - self.SQUARE * 2.5 \
                and x < self.current_piece.x - self.SQUARE * 1.5 \
                and y < self.current_piece.y - self.SQUARE * 1.5 + self.SQUARE * 4 \
                    * self.PIECE_COLORS_REVERSE.index(self.current_piece.color)\
                and y > self.current_piece.y - self.SQUARE * 2.5 + self.SQUARE * 4 \
                    * self.PIECE_COLORS_REVERSE.index(self.current_piece.color)


    def _new_click_within_right_king_valid_square_capture_move(self, x, y):
        '''
            Method -- _new_click_within_right_king_valid_square_capture_move
                helper method checks if the new click on a king piece is 
                within right valid squares for a capture move
            Parameters:
                self -- the current Move object
                x -- the x coordinate of the position that is to be checked
                y -- the y coordinate of the position that is to be checked
            Returns:
                True if the new click on a king piece is within right valid
                squares, or False if not.
        '''
        return x > self.current_piece.x + self.SQUARE * 1.5 \
                and x < self.current_piece.x + self.SQUARE * 2.5 \
                and y < self.current_piece.y - self.SQUARE * 1.5 + self.SQUARE * 4 \
                    * self.PIECE_COLORS_REVERSE.index(self.current_piece.color)\
                and y > self.current_piece.y - self.SQUARE * 2.5 + self.SQUARE * 4 * \
                    self.PIECE_COLORS_REVERSE.index(self.current_piece.color)
 