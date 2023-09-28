.text
.globl main

 main:
    addi    sp, sp, -16           # stack frame has 4 slots
    sw      ra, 12(sp)           
    sw      s0, 8(sp)                     
    addi    s0, sp, 16
    li      a0, 2                 # pass number 2 in a0
    j    twice                    # call twice  ***
    sw      a0, -12(s0)           # put return value to a
    li      a0, 0
    lw      ra, 12(sp)            
    lw      s0, 8(sp)            
    addi    sp, sp, 16           # restore sp

 twice:
    addi    sp, sp, -16          # create stack frame with 4 slots
    sw      ra, 12(sp)           # first slot keeps return address
    sw      s0, 8(sp)            # second slot keeps s0
    addi    s0, sp, 16           # set s0 to this stack frame
    sw      a0, -12(s0)          # store passing value (x) to slot 4
    lw      a0, -12(s0)          # get x
    add     a0, a0, a0           # x + x   return value in a0
    lw      ra, 12(sp)           # restore return address
    lw      s0, 8(sp)           
    addi    sp, sp, 16           # delete stack frame
    jalr    x0, x1, main
