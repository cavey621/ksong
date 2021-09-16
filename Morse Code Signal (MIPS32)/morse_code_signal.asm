# Skeleton file provided to students in UVic CSC 230, Summer 2021
# Original file copyright Mike Zastre, 2021


# Junyi Wei
# V00979016
# Assignment 2, CSC 230, Summer 2021


.text


main:	


# STUDENTS MAY MODIFY CODE BELOW
# vvvvvvvvvvvvvvvvvvvvvvvvvvvvvv

    ## Test code that calls procedure for part A
    #jal sos_send

    ## signal_flash test for part B
     #addi $a0, $zero, 0x24   # dot dot dash dot
     #jal signal_flash

    ## signal_flash test for part B
     #addi $a0, $zero, 0x73   # dash dash dash
     #jal signal_flash
        
    ## signal_flash test for part B
     #addi $a0, $zero, 0x23     # dot dash dot
     #jal signal_flash
            
    ## signal_flash test for part B
     #addi $a0, $zero, 0x11   # dash
     #jal signal_flash  
     
    ## signal_flash test for part B
     #addi $a0, $zero, 0xff   # space
     #jal signal_flash 
    
    # signal_message test for part C
     #la $a0, test_buffer
     #jal signal_message
    # signal_message test for part C
     #la $a0, test_buffer2
     #jal signal_message
    # one_alpha_encode test for part D
    # the letter 'p' is properly encoded as 0x64.
     #addi $a0, $zero, 'p'
     #jal one_alpha_encode  
    
    # one_alpha_encode test for part D
    # the letter 'a' is properly encoded as 0x12
     #addi $a0, $zero, 'a'
     #jal one_alpha_encode
    
    # one_alpha_encode test for part D
    # the space' is properly encoded as 0xff
     #addi $a0, $zero, ' '
     #jal one_alpha_encode
    
    # message_into_code test for part E
    # The outcome of the procedure is here
    # immediately used by signal_message
     la $a0, message11
     la $a1, buffer01
     jal message_into_code
     la $a0, buffer01
     jal signal_message
    

get_outta_here:
    # Proper exit from the program.
    addi $v0, $zero, 10
    syscall


	
###########
# PROCEDURE
sos_send:
	#dot
	jal seven_segment_on
	jal delay_short
	jal seven_segment_off
	jal delay_long
	
	#dot
	jal seven_segment_on
	jal delay_short
	jal seven_segment_off
	jal delay_long
	
	#dot
	jal seven_segment_on
	jal delay_short
	jal seven_segment_off
	jal delay_long
	
	#dash
	jal seven_segment_on
	jal delay_long
	jal seven_segment_off
	jal delay_long
	
	#dash
	jal seven_segment_on
	jal delay_long
	jal seven_segment_off
	jal delay_long
	
	#dash
	jal seven_segment_on
	jal delay_long
	jal seven_segment_off
	jal delay_long
	
	#dot
	jal seven_segment_on
	jal delay_short
	jal seven_segment_off
	jal delay_long
	
	#dot
	jal seven_segment_on
	jal delay_short
	jal seven_segment_off
	jal delay_long
	
	#dot
	jal seven_segment_on
	jal delay_short
	jal seven_segment_off
	jal delay_long
	
	jr $31


# PROCEDURE
signal_flash:
	addi $sp, $sp, -20
	sw $ra, 0($sp)
	sw $s0, 4($sp)
	sw $s1, 8($sp)
	sw $s2, 12($sp)
	sw $s4, 16($sp)
	
	
	beq $a0, 255, space_display
	beq $a0, 0xffffffff, space_display
	
	addi $s0, $zero, 15  # $s0 : value of ox0f
	and $s1, $a0, $s0   # $s1 : rightmost 4 digits
	
	add $s4, $a0, $zero  # $s4: save $a0 into $s4
	addi $t0, $zero, 4  # $t0: value of 4
	sub $t1, $t0, $s1 # $t1 : num of meaningless leading zeros
	
	beq $zero, $zero, process_leading_zeros

space_display:
	jal delay_long
	jal delay_long
	jal delay_long
	beq $zero, $zero, end_flash


process_leading_zeros:
	
	bne $t1, $zero, delete_leading_zero
	beq $zero, $zero, flash

	
flash:
	beq $s1, $zero, end_flash
	addi $t3, $zero, 128  # $t3 : value of 0b10000000
	and $t4, $s4, $t3          # $t4 : leftmost value of $s4
	
	beq $t4, 0, dot
	beq $t4, 128, dash


dot:
	jal seven_segment_on
	jal delay_short
	jal seven_segment_off
	jal delay_long
	beq $zero, $zero, move_left
			

dash:
	jal seven_segment_on
	jal delay_long
	jal seven_segment_off
	jal delay_long
	beq $zero, $zero, move_left

move_left:
	sll $s4, $s4, 1
	addi $s1, $s1, -1
	beq $zero, $zero, flash
	

delete_leading_zero:
	sll $s4, $s4, 1
	addi $t1, $t1, -1
	beq $zero, $zero, process_leading_zeros

end_flash:
	lw $ra, 0($sp)
	lw $s0, 4($sp)
	lw $s1, 8($sp)
	lw $s2, 12($sp)
	lw $s4, 16($sp)
	addi $sp, $sp, 20
	jr $ra

###########
# PROCEDURE
signal_message:
	addi $sp, $sp, -8
	sw $ra, 0($sp)
	sw $s0, 4($sp)

	add $s0, $a0, $zero # $s0 : store the value of $a0 (i.e. address of the message)
	beq $zero, $zero, loop_message

loop_message:
	
	lb $t0, 0($s0)
	beq $t0, $zero, finish_message
	add $a0, $t0, $zero
	jal signal_flash
	
	addi $s0, $s0, 1
	beq $zero, $zero, loop_message
	
	
finish_message:
	lw $ra, 0($sp)
	lw $s0, 4($sp)
	addi $sp, $sp, 8
	jr $ra
	
	
###########
# PROCEDURE
one_alpha_encode:
	addi $sp, $sp, -12
	sw $ra, 0($sp)
	sw $s0, 4($sp)
	sw $s1, 8($sp)
	
	
	beq $a0, ' ', process_space
	
	la $t0, codes # $t0 : the starting location of 'codes' in data memory
	sub $t1, $a0, 'a'   # $t1 : the distance from $a0 to 'a'
	
	sll $t1, $t1, 3  	#$t1 : 8 x the distance from $a0 to 'a' (i.e distance in the code label of data memory)
	add $t1, $t0, $t1 # t1: the memory address for the letter in $a0 
	
	add $s0, $zero, $zero #left most 4 digits
	add $s1, $zero, $zero #right most 4 digits

	addi $t1, $t1, 1 #starting form the first dot/dash location
	beq $zero, $zero, count_length


process_space:
	addi $v0, $zero, 0xff
	beq $zero, $zero, return_from_one_alpha_encode

count_length:
	
	lb $t2, 0($t1)  # $t2: the byte value in current $t1 addresss
	beq $t2, $zero, build_up_byte_sequence
	addi $s1, $s1, 1
	beq $t2, '-', add_one
	sll $s0, $s0, 1
	addi $t1, $t1, 1 
	beq $zero, $zero, count_length
	
add_one:
	sll $s0, $s0, 1
	addi $s0, $s0, 1
	
	addi $t1, $t1, 1 
	beq $zero, $zero, count_length	
	
build_up_byte_sequence:
	sll $s0, $s0, 4
	add $v0, $s0, $s1	
	beq $zero, $zero, return_from_one_alpha_encode
	
return_from_one_alpha_encode:
	lw $ra, 0($sp)
	lw $s0, 4($sp)
	lw $s1, 8($sp)
	
	addi $sp, $sp, 12
	jr $ra	


###########
# PROCEDURE
message_into_code:
	addi $sp, $sp, -8
	sw $ra, 0($sp)
	
	sw $s0, 4($sp)
	
	add $s0, $a0, $zero # $s0 : the copy of $a0
	beq $zero, $zero, loop_start

loop_start:
	lb $t0, 0($s0)
	beq $t0, $zero, returning_from_message_into_code
	add $a0, $zero, $t0
	jal one_alpha_encode
	sb $v0, 0($a1)
	addi $s0, $s0, 1
	addi $a1, $a1, 1
	beq $zero, $zero, loop_start

returning_from_message_into_code:
	lw $s0, 4($sp)
	lw $ra, 0($sp)
	addi $sp, $sp, 8
	jr $ra


# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# STUDENTS MAY MODIFY CODE ABOVE


#############################################
# DO NOT MODIFY ANY OF THE CODE / LINES BELOW

###########
# PROCEDURE
seven_segment_on:
	la $t1, 0xffff0010     # location of bits for right digit
	addi $t2, $zero, 0xff  # All bits in byte are set, turning on all segments
	sb $t2, 0($t1)         # "Make it so!"
	jr $31


###########
# PROCEDURE
seven_segment_off:
	la $t1, 0xffff0010	# location of bits for right digit
	sb $zero, 0($t1)	# All bits in byte are unset, turning off all segments
	jr $31			# "Make it so!"
	

###########
# PROCEDURE
delay_long:
	add $sp, $sp, -4	# Reserve 
	sw $a0, 0($sp)
	addi $a0, $zero, 600
	addi $v0, $zero, 32
	syscall
	lw $a0, 0($sp)
	add $sp, $sp, 4
	jr $31

	
###########
# PROCEDURE			
delay_short:
	add $sp, $sp, -4
	sw $a0, 0($sp)
	addi $a0, $zero, 200
	addi $v0, $zero, 32
	syscall
	lw $a0, 0($sp)
	add $sp, $sp, 4
	jr $31

#############
# DATA MEMORY
.data
codes:
    .byte 'a', '.', '-', 0, 0, 0, 0, 0
    .byte 'b', '-', '.', '.', '.', 0, 0, 0
    .byte 'c', '-', '.', '-', '.', 0, 0, 0
    .byte 'd', '-', '.', '.', 0, 0, 0, 0
    .byte 'e', '.', 0, 0, 0, 0, 0, 0
    .byte 'f', '.', '.', '-', '.', 0, 0, 0
    .byte 'g', '-', '-', '.', 0, 0, 0, 0
    .byte 'h', '.', '.', '.', '.', 0, 0, 0
    .byte 'i', '.', '.', 0, 0, 0, 0, 0
    .byte 'j', '.', '-', '-', '-', 0, 0, 0
    .byte 'k', '-', '.', '-', 0, 0, 0, 0
    .byte 'l', '.', '-', '.', '.', 0, 0, 0
    .byte 'm', '-', '-', 0, 0, 0, 0, 0
    .byte 'n', '-', '.', 0, 0, 0, 0, 0
    .byte 'o', '-', '-', '-', 0, 0, 0, 0
    .byte 'p', '.', '-', '-', '.', 0, 0, 0
    .byte 'q', '-', '-', '.', '-', 0, 0, 0
    .byte 'r', '.', '-', '.', 0, 0, 0, 0
    .byte 's', '.', '.', '.', 0, 0, 0, 0
    .byte 't', '-', 0, 0, 0, 0, 0, 0
    .byte 'u', '.', '.', '-', 0, 0, 0, 0
    .byte 'v', '.', '.', '.', '-', 0, 0, 0
    .byte 'w', '.', '-', '-', 0, 0, 0, 0
    .byte 'x', '-', '.', '.', '-', 0, 0, 0
    .byte 'y', '-', '.', '-', '-', 0, 0, 0
    .byte 'z', '-', '-', '.', '.', 0, 0, 0
    
message01:  .asciiz "a a a"
message02:  .asciiz "sos"
message03:  .asciiz "thriller"
message04:  .asciiz "billie jean"
message05:  .asciiz "the girl is mine"
message06:  .asciiz "pretty young thing"
message07:  .asciiz "human nature"
message08:  .asciiz "we are the world"
message09:  .asciiz "off the wall"
message10:  .asciiz "i want you back"
message11:  .asciiz "i love you"

buffer01:   .space 128
buffer02:   .space 128
test_buffer:    .byte 0x03 0x73 0x03 0x00    # This is SOS
