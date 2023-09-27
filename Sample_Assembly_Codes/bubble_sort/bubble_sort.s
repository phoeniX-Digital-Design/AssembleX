main:
    li sp, 4092
	addi sp, sp, -48
	sw s0, 44(sp)
	addi s0, sp, 48
	li a5, 3
	sw a5, -48(s0)
	li a5, 5
	sw a5, -44(s0)
	li a5, 1
	sw a5, -40(s0)
	li a5, 2
	sw a5, -36(s0)
	li a5, 4
	sw a5, -32(s0)
	sw x0, -20(s0)
	j two
six:
	sw	x0,-24(s0)
	j three
five:
	lw a5, -24(s0)
	slli a5, a5, 2
	addi a4, s0, -16
	add	a5, a4, a5
	lw a4, -32(a5)
	lw a5, -24(s0)
	addi a5, a5, 1
	slli a5, a5, 2
	addi a3, s0, -16
	add	a5, a3, a5
	lw a5, -32(a5)
	bge	a5, a4, four
	lw a5, -24(s0)
	slli a5, a5, 2
	addi a4, s0, -16
	add	a5, a4, a5
	lw a5, -32(a5)
	sw a5, -28(s0)
	lw a5, -24(s0)
	addi a5, a5, 1
	slli a5, a5, 2
	addi a4, s0, -16
	add	a5, a4, a5
	lw a4, -32(a5)
	lw a5, -24(s0)
	slli a5, a5, 2
	addi a3, s0, -16
	add	a5, a3, a5
	sw a4, -32(a5)
	lw a5, -24(s0)
	addi a5, a5, 1
	slli a5, a5, 2
	addi a4, s0, -16
	add	a5, a4, a5
	lw a4, -28(s0)
	sw a4, -32(a5)
four:
	lw a5, -24(s0)
	addi a5, a5 ,1
	sw a5, -24(s0)
three:
	li a4, 4
	lw a5, -20(s0)
	sub	a5, a4, a5
	lw a4, -24(s0)
	blt	a4, a5, five
	lw a5, -20(s0)
	addi a5, a5, 1
	sw a5, -20(s0)
two:
	lw a4, -20(s0)
	li a5, 3
	bge	a5, a4, six
	li a5, 0
	mv a0, a5
	lw s0, 44(sp)
	addi sp, sp, 48
    ebreak