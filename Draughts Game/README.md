# Draughts Game

This project is a graphical game of Checkers (AKA Draughts) 

Checkers Rules:
The game is played with black and red pieces on an 8x8 board with light and dark squares in a checkerboard pattern. The goal of the game is to capture all of your opponent’s pieces. 

Making moves
A turn consists of moving one of the player’s own pieces. ​Pieces may only be moved diagonally and in a forward direction​, with one exception (see “King pieces” below). “Forward” means from the player’s start side to the opposite side—red pieces move from the top of the board to the bottom, and black pieces move from the bottom to the top. There are two types of move a piece can make:
1. Non-capturing move​. A piece is moved diagonally forward one square. The square that the
        piece is moved to must be empty.
2.  Capturing move​. If an enemy piece is next to the player’s piece, and the next square in the same direction is empty, the enemy piece can be captured as long as the move is in a forward direction. The captured piece is removed from the board.

If a capture is possible, it must be made.​ Sometimes it’s possible to make multiple captures in a single move. Jumps can change diagonal direction, as long as the capturing piece continues forward. The two types of moves cannot be combined. For example, it is not possible to make a non-capturing move and continue on to make a capturing move in the same turn.

King pieces
When a piece gets all the way to the opposite side of the board, it is crowned a King. King pieces are very useful because they can move backwards as well as forwards. Moves are still diagonal. In “real” checkers, a King is made by stacking two pieces together. In my Python version of checkers, I identify King pieces with a white ring on the piece.

Ending the game
The game ends when a player has captured all enemy pieces (most common), or when one of the players is not able to move their remaining pieces.
