.globl dot
.text

dot:
    addi sp, sp, -24
    sw s0, 0(sp)     
    sw s1, 4(sp)        
    sw s2, 8(sp)        
    sw s3, 12(sp)       
    sw s4, 16(sp)       
    sw s5, 20(sp)       
    addi t5, x0, 1		