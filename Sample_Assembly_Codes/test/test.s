addi s0 x0 10 
loop:
	addi s0 s0 -1 
	beq s1 x0 out 
	beq x0 x0 loop
out:
	beq x0 x0 out