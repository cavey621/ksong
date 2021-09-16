	.globl main

	.data
KEYBOARD_EVENT_PENDING:
	.word	0x0
KEYBOARD_EVENT:
	.word   0x0
KEYBOARD_COUNTS:
	.space  128
NEWLINE:
	.asciiz "\n"
SPACE:
	.asciiz " "
	
	.eqv  LETTER_a 97
	.eqv  LETTER_space 32
	
	
	.text  
main:
# STUDENTS MAY MODIFY CODE BELOW
# vvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
	la $s0, 0xffff0000		# control register for MMIO Simulator "Receiver"
	lb $s1, 0($s0)
	ori $s1, $s1, 0x02		# Set bit 1 to enable "Receiver" interrupts (i.e., keyboard)
	sb $s1, 0($s0)
check_for_event:
   	la $s0, KEYBOARD_EVENT_PENDING 	# $s0 stores the address of KEYBOARD_EVENT_PENDING
   	lw $s1, 0($s0)			# $s1 stores the indicator value of KEYBOARD_EVENT_PENDING
   	
	beq $s1, $zero, check_for_event
	
	la $s2, KEYBOARD_EVENT
	lw $s2, 0($s2)			# $s2 stores the current key-pressed
	
	addi $s6, $zero, 26
	la $s3, KEYBOARD_COUNTS		# $s3 stores the starting address of the KEYBOARD_COUNTS
	add $t4, $zero, $s3		# $t4 currently holds the value in $s3 and will be dynamically changes in branch display_counts
	beq $s2, LETTER_space, display_counts
	
	 
	blt $s2, LETTER_a, reset
	bgt $s2, 122, reset
	
	
	sub $t2, $s2, LETTER_a 	
	sll $t2, $t2, 2			# $t2 is the address difference that key-pressed letter away from letter a
	
	add $s4, $s3, $t2 		# $s4 stores the address of the count of key-pressed letter in the array
	
	lw $s5, 0($s4)			# $s5 stores the key value
	addi $s5, $s5, 1
	sw $s5, 0($s4)			# increment the count for the key-pressed letter
	beq $zero, $zero, reset

	
display_counts:
	beq $s6, $zero, print_new_line
	sub $s6, $s6, 1
	
	lw $a0, 0($t4)
	addi $v0, $zero, 1
	syscall
	
	la $a0, SPACE
	addi $v0, $zero, 4
	syscall
			
	addi $t4, $t4, 4
	beq $zero, $zero, display_counts
	
print_new_line:
				
	la $a0, NEWLINE
	addi $v0, $zero, 4
	syscall
	
	beq $zero, $zero, reset		
							
reset:
	add $t0, $zero, $zero
	sw $t0, 0($s0) 			# reset the KEYBOARD_EVENT_PENDING to zero after finishing processing the key
	beq $zero, $zero, check_for_event


	.kdata

	.ktext 0x80000180
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

# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# STUDENTS MAY MODIFY CODE ABOVE	
