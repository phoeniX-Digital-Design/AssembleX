.globl dot
.text

dot:
    addi sp, sp, -24
    sw s0, 0(sp)        #sum
    sw s1, 4(sp)        #loaded val v0
    sw s2, 8(sp)        #loaded val v1
    sw s3, 12(sp)       #product
    sw s4, 16(sp)       #stride v0
    sw s5, 20(sp)       
    addi t5, x0, 1		