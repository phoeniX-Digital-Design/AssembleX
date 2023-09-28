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
    blt a2, t5, exit5
    blt a3, t5, exit6
    blt a4, t5, exit6
    j loop_start

exit5:
    li a1, 5
exit6:
    li a1, 6

loop_start:
	addi s0, x0, 0
    addi t0, x0, 0
    addi t1, x0, 0
    addi t2, x0, 0
    addi t3, x0, 4
    mul s4, a3, t3
    mul s5, a4, t3
    j loop_continue

loop_continue:
    beq t0, a2, loop_end
    lw s1, 0(a0)
    lw s2, 0(a1)
	add a0, a0, s4 
    add a1, a1, s5
    mul s3, s1, s2
    add s0, s0, s3
    addi t0, t0, 1
    j loop_continue

loop_end:
    mv a0, s0 
    lw s0, 0(sp) 
    lw s1, 4(sp)
    lw s2, 8(sp)
    lw s3, 12(sp)
    lw s4, 16(sp)
    lw s5, 20(sp)
    addi, sp, sp, 24
    ebreak