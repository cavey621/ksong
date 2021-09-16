# This code assumes the use of the "Bitmap Display" tool.
#
# Tool settings must be:
#   Unit Width in Pixels: 32
#   Unit Height in Pixels: 32
#   Display Width in Pixels: 512
#   Display Height in Pixels: 512
#   Based Address for display: 0x10010000 (static data)
#
# In effect, this produces a bitmap display of 16x16 pixels.


	.include "bitmap-routines.asm"

	.data
TELL_TALE:
	.word 0x12345678 0x9abcdef0	# Helps us visually detect where our part starts in .data section
	
	.globl main
	.text	
	
	.eqv DIAMOND_SIZE 7
	
main:
	addi $a0, $zero, 5
	addi $a1, $zero, 5
	addi $a2, $zero, 0x00ff0000
	jal draw_bitmap_diamond
	
	addi $a0, $zero, 12
	addi $a1, $zero, 9
	addi $a2, $zero, 0x0000ff00
	jal draw_bitmap_diamond
	
	addi $a0, $zero, 10
	addi $a1, $zero, 2
	addi $a2, $zero, 0x00ffffff
	jal draw_bitmap_diamond
	
	addi $a0, $zero, 2
	addi $a1, $zero, 14
	addi $a2, $zero, 0x000000ff
	jal draw_bitmap_diamond
	
	addi $a0, $zero, 7
	addi $a1, $zero, 5
	addi $a2, $zero, 0x00000000
	jal draw_bitmap_diamond

	addi $v0, $zero, 10
	syscall
	

# STUDENTS MAY MODIFY CODE BELOW
# vvvvvvvvvvvvvvvvvvvvvvvvvvvvvv

# Draws a 7x7 pixel diamond in the "Bitmap Display" tool
#
# $a0: row of diamond's midpoint
# $a1: column of diamond's midpoint
# $a2: colour of diamond
#
# The diamond will be seven pixels high, seven pixels wide
# (i.e. what is indicated by DIAMOND_SIZE).
#

draw_bitmap_diamond:
	addi $sp, $sp, -4
	sw $ra, 0($sp)
	
	# draw the middle line
	addi $a1, $a1, -3	# $a1 stores the column number of the left-most pixel in the line
	addi $a3, $zero, 7	# $a3 stores num of pixels in the line
	jal draw_line
	
	# draw the third line
	addi $a0, $a0, -1
	addi $a1, $a1, 1
	addi $a3, $zero, 5
	jal draw_line
	
	# draw the second line
	addi $a0, $a0, -1
	addi $a1, $a1, 1
	addi $a3, $zero, 3
	jal draw_line
	
	# draw the top line
	addi $a0, $a0, -1
	addi $a1, $a1, 1
	addi $a3, $zero, 1
	jal draw_line
	
	# draw the fifth line
	addi $a0, $a0, 4
	addi $a1, $a1, -2
	addi $a3, $zero, 5
	jal draw_line
	
	# draw the sixth line
	addi $a0, $a0, 1
	addi $a1, $a1, 1
	addi $a3, $zero, 3
	jal draw_line
	
	# draw the bottom line
	addi $a0, $a0, 1
	addi $a1, $a1, 1
	addi $a3, $zero, 1
	jal draw_line
	
	lw $ra, 0($sp)
	addi $sp, $sp, 4
	jr $ra



# Draws a line of pixels horizontally
#
# $a0: row number of the left-most pixel in the line
# $a1: column number of the left-most pixel in the line
# $a2: color of the pixels in the line
# $a3: num of pixels in the line
#

draw_line:
	addi $sp, $sp, -8
	sw $ra, 0($sp)
	sw $a1, 4($sp)
	beq $zero, $zero, process_line
	
process_line:
	beq $a3, $zero, complete_line	# check the num of pixels to be drawn
	addi $a3, $a3, -1
	jal set_pixel
	addi $a1, $a1, 1		# increment the column number (i.e. the next pixel in the line)
	beq $zero, $zero, process_line
	
complete_line:
	lw $ra, 0($sp)
	lw $a1, 4($sp)
	addi $sp, $sp, 8
	jr $ra


# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# STUDENTS MAY MODIFY CODE ABOVE
