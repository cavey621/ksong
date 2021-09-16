# Morse Code Signal

The signal encoding implemented for this project is based on the modern International Morse Code. This code in this project will turn a message to morse code and display by flash signal by 
"Digital Lab Sim”

The MARS application has the tool of “Digital Lab Sim”. This simulates a lab board with two seven-segment digital displays plus a hex keypad. The procedures seven_segment_on and seven_segment_off contain the code necessary to turn on and off all seven segments of the right-most digital display.

The structure of the file is as follows,

sos_send:
will flash the famous “SOS” morse code sequence (dot dot dot dash dash dash dot dot dot)
parameters: none 
return value: none

signal_flash:
takes a one-byte equivalent (passed into the procedure as the least-significant byte in a 32-bit register) and flashes the Digital Lab Sim display in a manner appropriate to the contents of that byte
parameters: one byte contained in the $a0 
register return value: none

signal_message:
use the address passed in $a0 as the starting location of the sequence, and then loop through that sequence, calling signal_flash for each byte, until encountering the end of the sequence. Once the sequence ends, the procedure must return.
parameters: data-memory address in $a0 
return value: none

one_alpha_encode:
Obtain the letter to be converted from input parameter $a0.
Locate in the table of codes the dot-dash sequence for the letter
Convert the dots (‘.’) and dashes (‘–’) and the length of the dot/dash sequence
into the one-byte equivalent for the letter.
parameters: data-memory address in $a0 
return value: one-byte equivalent stored in $v0


message_into_code:
(1) read each character in the original message, and for each character 
(2) convert it into one-byte equivalent by calling one_alpha_encode and storing its result into the buffer. 
and display the Morse code for a text message
parameters:
data-memory address of message in $a0
data-memory address of byte array to hold encoded message in $a1
return value: none
