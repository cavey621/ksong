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
KEYBOARD_EVENT_PENDING:
	.word	0x0
KEYBOARD_EVENT:
	.word   0x0
DIAMOND_ROW:
	.word	9
DIAMOND_COLUMN:
	.word	9
	
DIAMOND_COLOUR_1:
	.word 0x00db93c0
	
	.eqv LETTER_a 97
	.eqv LETTER_d 100
	.eqv LETTER_w 119
	.eqv LETTER_s 115
	.eqv LETTER_space 32
	
	.globl main
	
	.text	
main:
# STUDENTS MAY MODIFY CODE BELOW
# vvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
	# enable interrupts on MMIO Simulator "Receiver"
	la $s0, 0xffff0000		
	lb $s1, 0($s0)
	ori $s1, $s1, 0x02		# Set bit 1 to enable "Receiver" interrupts (i.e., keyboard)
	sb $s1, 0($s0)
	
	# initialize the diamond
	la $t0, DIAMOND_ROW
	lw $a0, 0($t0)
	la $t0, DIAMOND_COLUMN
	lw $a1, 0($t0)	
	la $t0, DIAMOND_COLOUR_1
	lw $a2, 0($t0)
	jal draw_bitmap_diamond
			
check_for_event:
   	la $s0, KEYBOARD_EVENT_PENDING 	# $s0 stores the address of KEYBOARD_EVENT_PENDING
   	lw $s1, 0($s0)			# $s1 stores the indicator value of KEYBOARD_EVENT_PENDING
	beq $s1, $zero, check_for_event
	la $s2, KEYBOARD_EVENT
	lw $s2, 0($s2)			# $s2 stores the current key-pressed
	beq $s2, LETTER_d, move_right
	beq $s2, LETTER_a, move_left
	beq $s2, LETTER_w, move_up
	beq $s2, LETTER_s, move_down
	beq $s2, LETTER_space, toggle_color
    	beq $zero, $zero, reset
   
move_right:
	jal erase_diamond
	la $t0, DIAMOND_ROW
	lw $a0, 0($t0)
	la $t0, DIAMOND_COLUMN
	lw $a1, 0($t0)
	addi $a1, $a1, 1
	sw $a1, 0($t0)			# update the diamond column value in memory
	la $t0, DIAMOND_COLOUR_1
	lw $a2, 0($t0)
	jal draw_bitmap_diamond
	beq $zero, $zero, reset

move_left:
	jal erase_diamond
	la $t0, DIAMOND_ROW
	lw $a0, 0($t0)
	la $t0, DIAMOND_COLUMN
	lw $a1, 0($t0)
	addi $a1, $a1, -1
	sw $a1, 0($t0)			# update the diamond column value in memory
	la $t0, DIAMOND_COLOUR_1
	lw $a2, 0($t0)
	jal draw_bitmap_diamond
	beq $zero, $zero, reset

move_up:
	jal erase_diamond
	la $t0, DIAMOND_ROW
	lw $a0, 0($t0)
	addi $a0, $a0, -1
	sw $a0, 0($t0)			# update the diamond row value in memory
	la $t0, DIAMOND_COLUMN
	lw $a1, 0($t0)
	la $t0, DIAMOND_COLOUR_1
	lw $a2, 0($t0)
	jal draw_bitmap_diamond
	beq $zero, $zero, reset
	
move_down:
	jal erase_diamond
	la $t0, DIAMOND_ROW
	lw $a0, 0($t0)
	addi $a0, $a0, 1
	sw $a0, 0($t0)			# update the diamond row value in memory
	la $t0, DIAMOND_COLUMN
	lw $a1, 0($t0)
	la $t0, DIAMOND_COLOUR_1
	lw $a2, 0($t0)
	jal draw_bitmap_diamond	
	beq $zero, $zero, reset

.data
	.eqv DIAMOND_COLOUR_DEFAULT 0x00db93c0
	.eqv DIAMOND_COLOUR_JUNYI 0x00979016
.text
toggle_color:
	la $t0, DIAMOND_ROW
	lw $a0, 0($t0)
	la $t0, DIAMOND_COLUMN
	lw $a1, 0($t0)
	la $t0, DIAMOND_COLOUR_1
	lw $a2, 0($t0)
	beq $a2, DIAMOND_COLOUR_DEFAULT, switch_to_junyi_color
	beq $a2, DIAMOND_COLOUR_JUNYI, switch_to_default_color
	beq $zero, $zero, reset
	
switch_to_junyi_color:
	addi $a2, $zero, DIAMOND_COLOUR_JUNYI
	beq $zero, $zero, finish_toggle_color
		
switch_to_default_color:
	addi $a2, $zero, DIAMOND_COLOUR_DEFAULT
	beq $zero, $zero, finish_toggle_color

finish_toggle_color:
	sw $a2, 0($t0)
	jal draw_bitmap_diamond
	beq $zero, $zero, reset

reset:
	add $t0, $zero, $zero
	sw $t0, 0($s0) 			# reset the KEYBOARD_EVENT_PENDING to zero after finishing processing the key
	beq $zero, $zero, check_for_event

    	# Should never, *ever* arrive at this point
    	# in the code.  
    	addi $v0, $zero, 10

.data
    	.eqv DIAMOND_COLOUR_BLACK 0x00000000
.text

    	addi $v0, $zero, DIAMOND_COLOUR_BLACK
    	syscall

# Draws a 7x7 pixel diamond in black color to cover the original diamond
#
# $a0: row of diamond's midpoint
# $a1: column of diamond's midpoint
# $a2: colour of diamond
#

erase_diamond:
	addi $sp, $sp, -4
	sw $ra, 0($sp)
	
	la $t0, DIAMOND_ROW
	lw $a0, 0($t0)
	la $t0, DIAMOND_COLUMN
	lw $a1, 0($t0)
	add $a2, $zero, DIAMOND_COLOUR_BLACK
	jal draw_bitmap_diamond

	lw $ra, 0($sp)
	addi $sp, $sp, 4
	jr $ra
	
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
 
# You can copy-and-paste some of your code from part (c)
# to provide the procedure body.
#
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
	addi $a1, $a1, 1		# increment the column number
	beq $zero, $zero, process_line
	
complete_line:
	lw $ra, 0($sp)
	lw $a1, 4($sp)
	addi $sp, $sp, 8
	jr $ra

	.kdata

	.ktext 0x80000180
#
# You can copy-and-paste some of your code from part (b)
# to provide elements of the interrupt handler.
#

__kernel_entry:
	mfc0 $k0, $13			# $13 is the "cause" register in Coproc0
	andi $k1, $k0, 0x7c		# bits 2 to 6 are the ExcCode field (0 for interrupts)
	srl  $k1, $k1, 2		# shift ExcCode bits for easier comparison
	beq $zero, $k1, __is_interrupt
	
__is_interrupt:
	andi $k1, $k0, 0x0100	# examine bit 8
	bne $k1, $zero, __is_keyboard_interrupt	 # if bit 8 set, then we have a keyboard interrupt.
	
	beq $zero, $zero, __exit_exception	# otherwise, we return exit kernel
	
__is_keyboard_interrupt:

	la $k0, 0xffff0004 		# $k0 is now storing the address of the data register of keyboard
	lw $k0, 0($k0) 			# $k0 is now storing the key-pressed 
	
	la $k1, KEYBOARD_EVENT		# $k1 is now storing the address of the KEYBOARD_EVENT in memory
	sw $k0, 0($k1) 			# store the key-pressed into the KEYBOARD_EVENT in memory

	la $k0, KEYBOARD_EVENT_PENDING  
	addi $k1, $zero, 1
	sw $k1, 0($k0)			# store value of 1 into the KEYBOARD_EVENT_PENDING to indicate a pending event 
	
	beq $zero, $zero, __exit_exception	# Kept here in case we add more handlers.

__exit_exception:
	eret

.data

# Any additional .text area "variables" that you need can
# be added in this spot. The assembler will ensure that whatever
# directives appear here will be placed in memory following the
# data items at the top of this file.


# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# STUDENTS MAY MODIFY CODE ABOVE


.eqv DIAMOND_COLOUR_WHITE 0x00FFFFFF
