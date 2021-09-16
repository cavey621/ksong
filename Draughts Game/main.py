'''
Kaiwei Song
CS 5001, Fall 2020
Final Project

This program will generate a graphical game of Checkers.
'''
import turtle
from piece import Piece
from gamestate import GameState
from move import Move
import random

NUM_SQUARES = 8 # The number of squares on each row.
SQUARE = 50 # The size of each square in the checkerboard.
SQUARE_COLORS = ("light gray", "white")
PIECE_COLORS = ("DarkRed", "black")
PIECE_COLORS_REVERSE = ("black", "DarkRed")
MOVETO_SQUARES = ('left', 'right')
g = GameState()
move = Move()


def click_handler(x, y):
    '''
        Function -- click_handler
            Called when a click occurs, advise when out of bound.
        Parameters:
            x -- X coordinate of the click. Automatically provided by Turtle.
            y -- Y coordinate of the click. Automatically provided by Turtle.
        Returns:
            Nothing.
    '''
    if not g.game_over:
        print("\nClicked at (" + str(x) + ', ' + str(y) + ')')
        if not is_valid_position(x, y):
            print("Not on the board!")
        else:
            turtle.penup()
            turtle.setposition(x, y)
            check_new_click()


def check_new_click():
    '''
        Function -- check_new_click
            Called when a click occurs, check its move state. If this is not
            a move, it should draw the potential move. If this is a move, it
            will determine it's a non-capture or capture move and implement
            the move accordingly.
        Parameters:
            Nothing.
        Returns:
            Nothing.
    '''
    
    pen = turtle.Turtle() 
    pen.penup()
    x, y = turtle.position()
    y = get_mid_point_of_square(y) # locate y coordinate of a piece
    x = get_mid_point_of_square(x) # locate x coordinate of a piece
    reset_grid_color = True

    color_this_turn = PIECE_COLORS[g.turn_counts % 2]  # determine the turn
    if not move.is_move:
        if exists_piece(x, y):
            the_piece = g.get_piece(x, y)
            if the_piece.color == color_this_turn:
                show_potential_moves(color_this_turn)
            else:
                print("This is not your piece.")
        else:
            print('This is an empty square.')
    else:
        if is_valid_non_capture_move(x, y):
            # reset the square to the current piece to empty
            reset_squares(move.current_piece.x - SQUARE / 2, \
                move.current_piece.y - SQUARE / 2, pen)
            # draw the piece to the new square after the move
            draw_piece(x, y - SQUARE / 2, pen, color_this_turn)
            # update the game state
            update_game_state_after_move(x, y)
            update_move_after_noncapture_move()
            reset_grid_color_black(pen) # set the grid to black
            check_and_upgrade_king(pen, move.current_piece)
            check_and_implement_computer_turn(color_this_turn)
        elif is_valid_capture_move(x, y):
            current_piece = move.current_piece
            # reset the square to the current piece to empty
            reset_squares(move.current_piece.x - SQUARE / 2, \
                move.current_piece.y - SQUARE / 2, pen)
            # draw the piece to the new square after the move
            draw_piece(x, y - SQUARE / 2, pen, color_this_turn)
            captured_piece = get_captured_piece(x, y, current_piece)
            # clear out the captured piece
            reset_squares(get_left_btm_point_of_square(captured_piece.x), \
                get_left_btm_point_of_square(captured_piece.y), pen)
            reset_grid_color_black(pen) # set the grid to black
            update_game_state_after_capture_move(captured_piece, \
                current_piece, x, y)
            update_move_after_capture_move(x, y)
            check_more_capture_move(current_piece, x, y, \
                color_this_turn, pen)
            check_and_upgrade_king(pen, move.current_piece)
            if not move.continue_capture_move:
                check_and_implement_computer_turn(color_this_turn)
        elif pick_another_piece(x, y, color_this_turn): 
            # rechoose another piece
            setup_show_potential_move()
            check_new_click()
        else:
            print('Please choose a red square to move.\n' + \
                'If capturing is available, you must capture it.')


def show_potential_moves(color_this_turn):
    '''
        Function -- show_potential_moves
            draws the potential move-to squares if the current click 
            is not in a moving state.
        Parameters:
            Nothing.
        Returns:
            Nothing.
    '''
    x, y = turtle.position()

    if exists_piece(x, y):
        pen = turtle.Turtle() # This variable does the drawing.
        pen.penup()
        reset_grid_color_black(pen)
        the_piece = g.get_piece(get_mid_point_of_square(x), \
            get_mid_point_of_square(y))
        x = get_left_btm_point_of_square(x)
        y = get_left_btm_point_of_square(y)
        pen.setposition(x, y)
        pen.color("Cyan")
        draw_square_outline(pen, SQUARE)
        pen.color("red")

        y_mid_point_in_second_left_right_square = y - SQUARE * 2 \
            + SQUARE * 4 * PIECE_COLORS.index(the_piece.color)
       
        move.is_non_capture_moving = True
        move.second_next_left_square_is_added = False

        draw_moveto_squares(the_piece, x, y, pen, \
            y_mid_point_in_second_left_right_square)
        draw_additional_moveto_squares_for_king(the_piece, x, y, pen)
        initiate_red_turn(color_this_turn)


def is_valid_non_capture_move(x, y):
    '''
        Function -- is_valid_non_capture_move
            determines if the current click is in a valid non-capture
            move-to squares.
        Parameters:
            x -- X coordinate of the position to be checked.
            y -- Y coordinate of the position to be checked. 
        Returns:
            True if the current click is in a valid non-capture move-to
            squares, False if not.
    '''

    return move.new_click_within_valid_squares_noncapture_move(x, y) \
        and move.is_non_capture_moving


def is_valid_capture_move(x, y):
    '''
        Function -- is_valid_capture_move
            determines if the current click is in a valid capture 
            move-to squares.
        Parameters:
            x -- X coordinate of the position to be checked.
            y -- Y coordinate of the position to be checked. 
        Returns:
            True if the current click is in a valid capture move-to
            squares, False if not.
    '''
    return not move.is_non_capture_moving \
        and move.new_click_within_valid_squares_capture_move(x, y)


def reset_squares(x, y, pen):
    '''
        Function -- reset_squares
            reset the board color to the original.
        Parameters:
            x -- X coordinate of the position.
            y -- Y coordinate of the position.
            pen -- an instance of Turtle.
        Returns:
            Nothing.
    '''    
    pen.setposition(x, y)
    pen.color('black', SQUARE_COLORS[0])
    draw_square(pen, SQUARE)


def draw_piece(x, y, pen, color_this_turn):
    '''
        Function -- draw_piece
            draw the piece in the color of current turn.
        Parameters:
            x -- X coordinate of the position.
            y -- Y coordinate of the position.
            pen -- an instance of Turtle.
            color_this_turn -- color in current turn.
        Returns:
            Nothing.
    '''    
    pen.setposition(x, y)
    pen.color('black', color_this_turn) 
    draw_circle(pen, SQUARE / 2)


def update_game_state_after_move(x, y):
    '''
        Function -- update_game_state_after_move
            update game state after move
        Parameters:
            x -- X coordinate of the current position.
            y -- Y coordinate of the current position.
        Returns:
            Nothing.
    '''   
    g.move_piece(move.current_piece, x, y) 
    g.turn_counts += 1


def update_move_after_noncapture_move():
    '''
        Function -- update_move_after_noncapture_move
            update move after non-capture move
        Parameters:
            Nothing.
        Returns:
            Nothing.
    '''   
    move.is_non_capture_moving = False # turn off the 'is_moving' status
    move.valid_moveto_squares = [] # reset the moveto_squares to empty
    move.second_next_left_square_is_added = False
    move.is_move = False


def get_captured_piece(x, y, current_piece):
    '''
        Function -- get_captured_piece
            get the captured piece
        Parameters:
            x -- X coordinate of the current position.
            y -- Y coordinate of the current position.
            current_piece -- the current implementing instance of Piece
        Returns:
            the instance of Piece for the captured piece.
    '''   
    x_captured_piece = x - SQUARE if x > current_piece.x else x + SQUARE
    # check to see if the piece if going forward or backward
    if current_piece.is_king and king_moves_backwards(current_piece, y):
        y_captured_piece = y + SQUARE - SQUARE * 2 * \
            PIECE_COLORS_REVERSE.index(current_piece.color)
    else:
        y_captured_piece = y + SQUARE - SQUARE * 2 * \
            PIECE_COLORS.index(current_piece.color)
    return g.get_piece(x_captured_piece, y_captured_piece)


def update_game_state_after_capture_move(captured_piece, current_piece, x, y):
    '''
        Function -- update_game_state_after_capture_move
            update game state after capture move
        Parameters:
            captured_piece -- the instance of Piece for the captured piece.
            current_piece -- the current implemented instance of Piece.
            x -- X coordinate of the current position.
            y -- Y coordinate of the current position.
        Returns:
            Nothing.
    '''   
    g.remove_piece(captured_piece)
    g.move_piece(current_piece, x, y) # update the piece location


def update_move_after_capture_move(x, y):
    '''
        Function -- update_move_after_capture_move
            update move after the capture move
        Parameters:
            x -- X coordinate of the current position.
            y -- Y coordinate of the current position.
        Returns:
            Nothing.
    '''   
    move.is_non_capture_moving = False 
    move.valid_moveto_squares = [] # reset the moveto_squares to empty
    move.second_next_left_square_is_added = False
    move.current_piece = g.get_piece(x, y)
    move.continue_capture_move = False


def has_more_capture_moves(the_piece, x, y):
    '''
        Function -- has_more_capture_moves
            check if the current captured move has more available
            captured moves 
        Parameters:
            x -- X coordinate of the current position.
            y -- Y coordinate of the current position.
        Returns:
            True if the current captured move has more available
            captured moves, False if not.
    ''' 
    has_more = \
        is_enemy_piece(the_piece, x - SQUARE, y - SQUARE + SQUARE * 2 \
            * PIECE_COLORS.index(the_piece.color)) \
        and is_empty_moveto_square(the_piece, x - SQUARE * 1.5, \
            y - SQUARE * 1.5 + SQUARE * 2 * \
            PIECE_COLORS.index(the_piece.color), MOVETO_SQUARES[0]) \
        or is_enemy_piece(the_piece, x + SQUARE, y - SQUARE + SQUARE * 2 * \
            PIECE_COLORS.index(the_piece.color))\
        and is_empty_moveto_square(the_piece, x + SQUARE / 2, \
            y - SQUARE * 1.5 + SQUARE * 2 * PIECE_COLORS.index(the_piece.color), \
            MOVETO_SQUARES[1])
    
    if the_piece.is_king:
        king_has_more = \
        is_enemy_piece(the_piece, x - SQUARE, \
            y - SQUARE + SQUARE * 2 * PIECE_COLORS_REVERSE.index(the_piece.color)) \
        and is_empty_move_square_for_king(the_piece, x - SQUARE * 1.5, \
            y - SQUARE * 1.5 + SQUARE * 2 * \
            PIECE_COLORS_REVERSE.index(the_piece.color), MOVETO_SQUARES[0]) \
        or is_enemy_piece(the_piece, x + SQUARE, \
            y - SQUARE + SQUARE * 2 * PIECE_COLORS_REVERSE.index(the_piece.color)) \
        and is_empty_move_square_for_king(the_piece, x + SQUARE / 2, \
            y - SQUARE * 1.5 + SQUARE * 2 * \
            PIECE_COLORS_REVERSE.index(the_piece.color), MOVETO_SQUARES[1])
        return has_more or king_has_more
    else:
        return has_more


def setup_show_potential_move():
    '''
        Function -- setup_show_potential_move
            reset the some attributes in Move instance to default.
        Parameters:
            Nothing.
        Returns:
            Nothing.
    ''' 
    move.valid_moveto_squares = []
    move.is_move = False
    move.second_next_left_square_is_added = False


def check_more_capture_move(current_piece, x, y, color_this_turn, pen):
    '''
        Function -- check_more_capture_move
            if has more capture moves, continue to show the potential moves, 
            otherwise, update the game state and reset the move to default.
        Parameters:
            current_piece -- the current implemented instance of Piece.
            x -- X coordinate of the current position.
            y -- Y coordinate of the current position.
            color_this_turn -- color in current turn.
            pen -- an instance of Turtle.
        Returns:
            Nothing.
    ''' 
    if has_more_capture_moves(current_piece, x, y):
        
        move.valid_moveto_squares = [] # reset the moveto_squares to empty
        move.second_next_left_square_is_added = False
        show_potential_moves(color_this_turn)
        move.continue_capture_move = True
    else:    
        update_game_state_after_move(x, y)
        reset_grid_color_black(pen) # set the grid to black
        setup_show_potential_move()
        move.is_non_capture_moving = False # turn off the 'is_moving' status
        move.continue_capture_move = False


def pick_another_piece(x, y, color_this_turn):
    '''
        Function -- pick_another_piece
            check if it is valid to choose another piece to move.
        Parameters:
            current_piece -- the current implemented instance of Piece.
            x -- X coordinate of the current position.
            y -- Y coordinate of the current position.
            color_this_turn -- color in current turn.
        Returns:
            Nothing.
    ''' 
    return exists_piece(x, y) and g.get_piece(x, y).color == color_this_turn \
            and not move.continue_capture_move


def is_game_over():
    '''
        Function -- is_game_over
            check if the game result comes out.
        Parameters:
            Nothing.
        Returns:
            True if the game is over, otherwise False.
    ''' 
    if len(g.black_pieces) == 0:
        print('############# You lost! #############')
        g.game_over = True
        return True
    if len(g.red_pieces) == 0:
        print('************* Congratulations! You win! *************')
        g.game_over = True
        return True
    return False


def check_and_implement_computer_turn(color_this_turn):
    '''
        Function -- check_and_implement_computer_turn
            if the game is not over and it's computer turn, get a random 
            red piece. if all the remaining pieces have been picked but 
            no more possible moves, it should throw recursion error which
            also means the player has won the game.
        Parameters:
            color_this_turn -- color in current turn.
        Returns:
            Nothing.
    ''' 
    try:
        if not is_game_over():
            if color_this_turn == PIECE_COLORS[1]:
                random_red_piece = get_random_red_piece()
                x = random_red_piece.x
                y = random_red_piece.y
                turtle.setposition(x, y)
                check_new_click()
    except RecursionError:
        print('All red pieces were blocked.')
        print('************* Congratulations! You win! *************')
        g.game_over = True


def draw_moveto_squares(the_piece, x, y, pen, y_mid_point_in_second_left_right_square):
    '''
        Function -- draw_moveto_squares
            draw all the possible move-to squares.
        Parameters:
            the_piece -- the current instance of Piece.
            x -- X coordinate of the current position.
            y -- Y coordinate of the current position.
            pen -- an instance of Turtle.
            y_mid_point_in_second_left_right_square --
                Y coordinate of the midpoint in 
            the second next piece in all diagonal directions.
        Returns:
            Nothing.
    ''' 
    for side in MOVETO_SQUARES:
        if is_empty_moveto_square(the_piece, x, y, side):

            draw_moving_square(pen, the_piece, side, \
                x - SQUARE + SQUARE * 2 * MOVETO_SQUARES.index(side), \
                    y - SQUARE + SQUARE * 2 * PIECE_COLORS.index(the_piece.color))
            move.is_move = True
            if side == MOVETO_SQUARES[0] or side == MOVETO_SQUARES[1] \
                and not move.second_next_left_square_is_added:
                move.valid_moveto_squares.append(side)

        elif is_enemy_piece(the_piece, \
                x - SQUARE / 2 + SQUARE * 2 * MOVETO_SQUARES.index(side), \
                y - SQUARE / 2 + SQUARE * 2 * PIECE_COLORS.index(the_piece.color)) \
                and is_empty_moveto_square(the_piece, \
                    x - SQUARE + SQUARE * 2 * MOVETO_SQUARES.index(side), \
                        y - SQUARE + SQUARE * 2 * PIECE_COLORS.index(the_piece.color), side):
                draw_moving_square(pen, the_piece, side, \
                    x - SQUARE * 2 + SQUARE * 4 * MOVETO_SQUARES.index(side), \
                    y_mid_point_in_second_left_right_square)
                move.is_move = True
                move.is_non_capture_moving = False
                if side == MOVETO_SQUARES[0]:
                    move.valid_moveto_squares.append(side)
                    move.second_next_left_square_is_added = True
                if side == MOVETO_SQUARES[1] and move.second_next_left_square_is_added:
                    move.valid_moveto_squares.append(side)
                elif side == MOVETO_SQUARES[1] and not move.second_next_left_square_is_added:
                    move.valid_moveto_squares = [side]


def draw_additional_moveto_squares_for_king(the_piece, x, y, pen):
    '''
        Function -- draw_additional_moveto_squares_for_king
            draw additional possible move-to squares for the king piece.
        Parameters:
            the_piece -- the current instance of Piece.
            x -- X coordinate of the current position.
            y -- Y coordinate of the current position.
            pen -- an instance of Turtle.
        Returns:
            Nothing.
    ''' 
    KING_MARK = '_king'
    if the_piece.is_king:
        y_mid_point_in_second_left_right_square_for_king = \
            y - SQUARE * 2 + SQUARE * 4 * PIECE_COLORS_REVERSE.index(the_piece.color)

        for side in MOVETO_SQUARES:
            if is_empty_move_square_for_king(the_piece, x, y, side):

                draw_moving_square(pen, the_piece, side, \
                    x - SQUARE + SQUARE * 2 * MOVETO_SQUARES.index(side), \
                    y - SQUARE + SQUARE * 2 * PIECE_COLORS_REVERSE.index(the_piece.color))
                move.is_move = True
                if move.is_non_capture_moving:
                    move.valid_moveto_squares.append(side + KING_MARK)

            elif is_enemy_piece(the_piece, \
                x - SQUARE / 2 + SQUARE * 2 * MOVETO_SQUARES.index(side), \
                    y - SQUARE / 2 + SQUARE * 2 * PIECE_COLORS_REVERSE.index(the_piece.color)) \
                and is_empty_move_square_for_king(the_piece, \
                    x - SQUARE + SQUARE * 2 * MOVETO_SQUARES.index(side), \
                        y - SQUARE + SQUARE * 2 * PIECE_COLORS_REVERSE.index(the_piece.color), \
                            side):

                    draw_moving_square(pen, the_piece, side, \
                        x - SQUARE * 2 + SQUARE * 4 * MOVETO_SQUARES.index(side), \
                            y_mid_point_in_second_left_right_square_for_king)
                    move.is_move = True                
                    if side == MOVETO_SQUARES[0] and move.is_non_capture_moving:
                        move.valid_moveto_squares = [side + KING_MARK]
                    elif side == MOVETO_SQUARES[0] and not move.is_non_capture_moving:
                        move.valid_moveto_squares.append(side + KING_MARK)
                    if side == MOVETO_SQUARES[1] and move.is_non_capture_moving:
                        move.valid_moveto_squares = [side + KING_MARK]
                    elif side == MOVETO_SQUARES[1] and not move.is_non_capture_moving:
                        move.valid_moveto_squares.append(side + KING_MARK)
                    move.is_non_capture_moving = False


def is_red_turn(color_this_turn):
    '''
        Function -- is_red_turn
            check if this is the red turn.
        Parameters:
            color_this_turn -- color in current turn.
        Returns:
            True if this is the red turn, False if not.
    ''' 
    return color_this_turn == PIECE_COLORS[0]


def initiate_red_turn(color_this_turn):
    '''
        Function -- initiate_red_turn
            if current turn is red turn, select a random red piece and starts the 
            red turn, if the selected red pieced has no valid move-to squares,
            reselect another red piece until there is at least one valid move-to
            square.
        Parameters:
            color_this_turn -- color in current turn.
        Returns:
            Nothing.
    ''' 
    if is_red_turn(color_this_turn):
        if len(move.valid_moveto_squares) == 0:
            random_red_piece = get_random_red_piece()
            turtle.setposition(random_red_piece.x, random_red_piece.y)
            show_potential_moves(color_this_turn)
        else:
            x, y = get_random_position_in_valid_area()
            turtle.setposition(x, y)
            check_new_click()


def get_random_red_piece():
    '''
        Function -- get_random_red_piece
            randomly select a red piece.
        Parameters:
            Nothing.
        Returns:
            Nothing.
    ''' 
    num_red_piece = len(g.red_pieces)
    rand = random.randint(0, num_red_piece - 1)
    rand_red_piece = g.red_pieces[rand]
    move.current_piece = rand_red_piece
    return rand_red_piece


def get_random_position_in_valid_area():
    '''
        Function -- get_random_position_in_valid_area
            Once the valid move-to suqares are availale, pick one square to move to.
        Parameters:
            Nothing.
        Returns:
            the (x, y) of the selected move-to position.
    ''' 
    valid_positions_lst = []
    for x in range(-SQUARE * 4, SQUARE * 4):
        for y in range(-SQUARE * 4, SQUARE * 4):
            if move.is_non_capture_moving and \
                move.new_click_within_valid_squares_noncapture_move(x, y) \
                or not move.is_non_capture_moving \
                    and move.new_click_within_valid_squares_capture_move(x, y):
                valid_positions_lst.append((x, y))
                
    rand = random.randrange(len(valid_positions_lst))
    return valid_positions_lst[rand]


def is_empty_moveto_square(the_piece, x, y, side):
    '''
        Function -- is_empty_moveto_square
            Check if the move-to suqare is empty.
        Parameters:
            the_piece -- the current instance of Piece.
            x -- X coordinate of the current position.
            y -- Y coordinate of the current position.
            side -- a string indicating the 'left' side or 'right' side 
        Returns:
            True if the move-to suqare is empty, False if not.
    ''' 
    is_empty = not g.exists_piece(x - SQUARE / 2 + 2 * SQUARE * MOVETO_SQUARES.index(side), \
        y - SQUARE / 2 + 2 * SQUARE * PIECE_COLORS.index(the_piece.color)) \
            and is_valid_position(x - SQUARE + SQUARE * 2 * MOVETO_SQUARES.index(side), \
                y - SQUARE + SQUARE * 2 * PIECE_COLORS.index(the_piece.color))
    return is_empty


def is_empty_move_square_for_king(the_piece, x, y, side):
    '''
        Function -- is_empty_move_square_for_king
            Check if the move-to suqare is empty for a king piece.
        Parameters:
            the_piece -- the current instance of Piece.
            x -- X coordinate of the current position.
            y -- Y coordinate of the current position.
            side -- a string indicating the 'left' side or 'right' side 
        Returns:
            True if the move-to suqare is empty for a king piece, False if not.
    ''' 
    if the_piece.is_king:
        is_empty = \
            not g.exists_piece(x - SQUARE / 2 + 2 * SQUARE * MOVETO_SQUARES.index(side), \
            y - SQUARE / 2 + 2 * SQUARE * PIECE_COLORS_REVERSE.index(the_piece.color)) \
        and is_valid_position(x - SQUARE + SQUARE * 2 * MOVETO_SQUARES.index(side), \
            y - SQUARE + SQUARE * 2 * PIECE_COLORS_REVERSE.index(the_piece.color))
    return is_empty


def is_enemy_piece(the_piece, target_x, target_y):
    '''
        Function -- is_enemy_piece
            Check if a piece is an enemy piece.
        Parameters:
            the_piece -- the current instance of Piece.
            target_x -- X coordinate of the position to be checked.
            target_y -- Y coordinate of the position to be checked.
        Returns:
            True if the piece is an enemy piece, False if not.
    ''' 
    return g.exists_piece(target_x, target_y) and is_valid_position(target_x, target_y) \
        and g.get_piece(target_x, target_y).color != the_piece.color


      
def check_and_upgrade_king(pen, current_piece):
    '''
        Function -- check_and_upgrade_king
            Check if the current piece becomes a king, if yes upgrade it.
        Parameters:
            pen -- an instance of Turtle.
            current_piece -- the current instance of Piece.
        Returns:
            Nothing.
    ''' 
    x = current_piece.x
    y = current_piece.y
    if is_valid_position(x, y):
        if y > SQUARE * 3 and current_piece.color == PIECE_COLORS[1]\
            or y < -SQUARE * 3 and current_piece.color == PIECE_COLORS[0] \
                or current_piece.is_king:
            upgrade_king(pen, current_piece)
            current_piece.is_king = True


def upgrade_king(pen, current_piece):
    '''
        Function -- upgrade_king
            draw the crown mark on the king piece.
        Parameters:
            pen -- an instance of Turtle.
            current_piece -- the current instance of Piece.
        Returns:
            Nothing.
    ''' 
    pen.penup()
    radius = 5
    pen.setposition(current_piece.x, current_piece.y - radius)
    king_color = 'misty rose' if current_piece.color == PIECE_COLORS[0] else 'papaya whip'
    pen.color(king_color, king_color)
    pen.begin_fill()
    draw_crown(pen, radius)
    pen.end_fill()
    pen.penup()


def king_moves_backwards(current_piece, y):
    '''
        Function -- king_moves_backwards
            check if a king is moveing backwards (in an opposite direction to its orginal
            moving direction).
        Parameters:
            current_piece -- the current instance of Piece.
            y -- the Y coordinate of the moveing postion.
        Returns:
            True if the king is moveing backwards, False if not.
    ''' 
    backwards = False
    if current_piece.color == PIECE_COLORS[0] and y > current_piece.y:
        backwards = True  
    if current_piece.color == PIECE_COLORS[1] and y < current_piece.y:
        backwards = True
    return backwards


def draw_crown(pen, half_base_length):
    '''
        Function -- draw_crown
            draw the crown on to the king piece during its upgrading process.
        Parameters:
            pen -- an instance of Turtle.
            half_base_length -- the half of the base length of the crown.
        Returns:
            Nothing.
    ''' 
    LEN_SIDE = 60
    pen.pendown()
    pen.forward(half_base_length)
    pen.left(LEN_SIDE)
    pen.forward(half_base_length)
    pen.left(LEN_SIDE * 2)
    pen.forward(half_base_length)
    pen.right(LEN_SIDE)
    pen.forward(half_base_length)
    pen.left(LEN_SIDE * 2)
    pen.forward(half_base_length)
    pen.right(LEN_SIDE)
    pen.forward(half_base_length)
    pen.left(LEN_SIDE * 2)
    pen.forward(half_base_length)
    pen.left(LEN_SIDE)
    pen.forward(half_base_length)
    pen.penup()


def draw_moving_square(pen, the_piece, side, x, y):
    '''
        Function -- draw_moving_square
            draw the square to move.
        Parameters:
            pen -- an instance of Turtle.
            the_piece -- the current instance of Piece.
            side -- a string indicating the 'left' side or 'right' side.
            x -- X coordinate of the move-to position.
            y -- Y coordinate of the move-to position.
        Returns:
            Nothing.
    ''' 
    pen.setposition(x, y)
    draw_square_outline(pen, SQUARE)
    move.current_piece = the_piece


def is_valid_position(x, y):
    '''
        Function -- is_valid_position
            check if the position is on the board.
        Parameters:
            x -- X coordinate of the position to be checked.
            y -- Y coordinate of the position to be checked.
        Returns:
            True if the position is on the board, False if not.
    ''' 
    is_valid_x = x >= -NUM_SQUARES * SQUARE / 2 and x < NUM_SQUARES * SQUARE / 2
    is_valid_y = y >= -NUM_SQUARES * SQUARE / 2 and y < NUM_SQUARES * SQUARE / 2
    return is_valid_x and is_valid_y


def get_mid_point_of_square(num):
    '''
        Function -- get_mid_point_of_square
            returns the mid point of a number.
        Parameters:
            num -- the number to get the mid point from.
        Returns:
            the mid point of the number num.
    ''' 
    return get_multiple_square(num + SQUARE * 4) * SQUARE - SQUARE * 3.5


def exists_piece(x, y):
    '''
        Function -- exists_piece
            check if the positon exists a piece.
        Parameters:
            x -- X coordinate of the position to be checked.
            y -- Y coordinate of the position to be checked.
        Returns:
            True if the position exists a piece, False if not.
    ''' 
    return g.exists_piece(get_mid_point_of_square(x), get_mid_point_of_square(y))


def get_left_btm_point_of_square(num):
    '''
        Function -- get_left_btm_point_of_square
            calculate the left bottom point of a number.
        Parameters:
            num -- the number to get the left bottom point from.
        Returns:
            the left bottom point of a number.
    ''' 
    return get_multiple_square(num + SQUARE * 4) * SQUARE - SQUARE * 4


def reset_grid_color_black(a_turtle):
    '''
        Function -- reset_grid_color_black
            reset all the grid color to black
        Parameters:
            a_turtle -- an instance of Turtle.
    ''' 
    for i in range(NUM_SQUARES):
        for j in range(NUM_SQUARES):         
            if j % 2 != i % 2:
                a_turtle.setposition(-SQUARE * 4 + SQUARE * j, -SQUARE * 4 + SQUARE * i)
                draw_square_outline(a_turtle, SQUARE)


def get_multiple_square(num):
    '''
        Function -- get_multiple_square
            returns the number of 50 included in the num.
        Parameters:
            num -- the number to get the multiple from.
        Returns:
            the number of 50 included in the num
    ''' 
    multiple = 0
    while num > 0:
        num = num - SQUARE
        multiple += 1
    return multiple - 1


def draw_line(a_turtle, length):
    '''
        Function -- draw_line
            Draw a line of a given length.
        Parameters:
            a_turtle -- an instance of Turtle
            length -- the length of the line
        Returns:
            Nothing. Draws the line in the graphics window.
    '''
    a_turtle.pendown()
    a_turtle.forward(length)
    a_turtle.penup()


def draw_square(a_turtle, size):
    '''
        Function -- draw_square
            Draw a square of a given size and fill the color in.
        Parameters:
            a_turtle -- an instance of Turtle
            size -- the length of each side of the square
        Returns:
            Nothing. Draws a square in the graphics window.
    '''
    RIGHT_ANGLE = 90

    a_turtle.pendown()
    a_turtle.begin_fill()
    for i in range(4):
        a_turtle.forward(size)
        a_turtle.left(RIGHT_ANGLE)
    a_turtle.end_fill()
    a_turtle.penup()


def draw_square_outline(a_turtle, size):
    '''
        Function -- draw_square
            Draw a square of a given size and fill the color in.
        Parameters:
            a_turtle -- an instance of Turtle
            size -- the length of each side of the square
        Returns:
            Nothing. Draws a square in the graphics window.
    '''
    RIGHT_ANGLE = 90

    a_turtle.pendown()
    for i in range(4):
        a_turtle.forward(size)
        a_turtle.left(RIGHT_ANGLE)
    a_turtle.penup()

def draw_circle(a_turtle, radius):
    '''
        Function -- draw_circle
            Draw a circle with a given radius and fill the color in.
        Parameters:
            a_turtle -- an instance of Turtle
            radius -- the radius of the circle
        Returns:
            Nothing. Draws a circle in the graphics window.
    '''
    a_turtle.pendown()
    a_turtle.begin_fill()
    a_turtle.circle(radius)
    a_turtle.end_fill()
    a_turtle.penup()


def draw_pieces(a_turtle, radius, piece_color, starting_x, starting_y):
    '''
        Function -- draw_pieces
            Draw all the pieces for one party.
        Parameters:
            a_turtle -- an instance of Turtle.
            radius -- the radius of the circle.
            piece_color -- the fill color of the pieces.
            starting_x -- the x_coordinate of the first piece to draw.
            starting_y -- the y_coordinate of the first piece to draw.
        Returns:
            Nothing. Draws all the pieces for one party in the graphics window.
    '''
    NUM_PIECES_IN_ROW = 4
    NUM_ROWS = 3
    a_turtle.color("black", piece_color)
    original_starting_x = starting_x
    for row in range(NUM_ROWS):
        starting_x = starting_x + SQUARE - (2 * SQUARE * PIECE_COLORS.index(piece_color)) \
             if row % 2 == 1 else original_starting_x
        # increment starting_x by SQUARE if darkred, decrement if black, for the middle row
        for piece in range(NUM_PIECES_IN_ROW):
            a_turtle.setposition(starting_x + (2 * SQUARE) * piece, starting_y)
            draw_circle(a_turtle, radius)
        starting_y += SQUARE


def main():
    board_size = NUM_SQUARES * SQUARE
    # Create the UI window. This should be the width of the board plus a little margin
    window_size = board_size + SQUARE # The extra + SQUARE is the margin
    turtle.setup(window_size, window_size)

    # Set the drawing canvas size. The should be actual board size
    turtle.screensize(board_size, board_size)
    turtle.bgcolor("white") # The window's background color
    turtle.tracer(0, 0) # makes the drawing appear immediately

    pen = turtle.Turtle() # This variable does the drawing.
    pen.penup() # This allows the pen to be moved.
    pen.hideturtle() # This gets rid of the triangle cursor.

    pen.color("black", "white") # The first parameter is the outline color, 
                                # the second is the fille

    # YOUR CODE HERE
    cornor = -board_size / 2
    pen.setposition(cornor, cornor)
    draw_square(pen, board_size)

    pen.color('black', SQUARE_COLORS[0])

    # Draw the panel with gray and white fill
    for i in range(NUM_SQUARES):
        for j in range(NUM_SQUARES):         
            if j % 2 != i % 2:
                pen.setposition(cornor + SQUARE * j, cornor + SQUARE * i)
                draw_square(pen, SQUARE)

    # Draw pieces in the starting postion for black and red pieces
    draw_pieces(pen, SQUARE / 2, PIECE_COLORS[1], cornor + SQUARE * 1.5, cornor) # black
    draw_pieces(pen, SQUARE / 2, PIECE_COLORS[0], cornor + SQUARE * 0.5, SQUARE) # red


    # Click handling
    screen = turtle.Screen()
    screen.onclick(click_handler) # This will call the click_handler function 
    turtle.done() # Stops the window from closing.


if __name__ == "__main__":
    main()
