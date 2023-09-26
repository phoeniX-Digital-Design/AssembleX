main:
	addi sp, x0, 512
	addi sp, sp, -48
	addi s0, sp, 48
    li a5, 10
    sw a5, -48(s0)
    li a5, 324
    sw a5, -44(s0)
    li a5, 45
    sw a5, -40(s0)
    li a5, 90
    sw a5, -36(s0)
    li a5, 216
    sw a5, -32(s0)
    addi s1, s0, 0
    addi s2, s0, 20
    mv t1, x0
swap:
    mv t0, t1
load:
    lw  t1, -48(s1)
    addi s1, s1, 4
    bge t1, t0, swap 
    blt s1, s2, load
    sw t0, -28(s0)
    