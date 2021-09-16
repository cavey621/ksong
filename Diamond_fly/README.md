# Diamond_fly

keyboard_handler.asm
contains an interrupt handler for the “Keyboard and Display MMIO Simulator” tool. The handler is to transfer the pressed-key’s value into data memory, and indicate that a keyboard event is “pending”. If the space key is pressed, the counts are output on the “Mars messages” pane (again through code outside of .ktext). Counts for the total-keypress- so-far of each lower-case letter are to be output. After finishing all processing for a keypress, the program  now indicate there is no longer a pending keyboard event.

draw_bitmap_diamond.asm
takes the parameters and draws a seven-by-seven bitmap diamond where row/column location centre pixel of that diamond is given as the first two parameters in this procedure.

diamond_move.asm
combines the keyboard interrupts and the bitmap display in order to control the movement of a seven-by-seven diamond on the display.
Initially the seven-by-seven diamond will located somewhat off-centre in the display. The following keys will “move” the diamond:
• ‘d’:move the diamond right by one pixel
• ‘a’:move the diamond left by one pixel
• ‘w’:move the diamond up by one pixel
• ‘s’:move the diamond down by one pixel
• space: toggle the colour of the diamond from the default to user-customized color

bitmap-routines.asm
contains the base set-up code for other files to run
