.text
.globl main
main:
  # Array setup
  li a0, 8                       # Array length
  # Binary search
  li t0, 0                       # Left pointer
  addi t1, a0, -1                # Right pointer

loop:
  blt t0, t1, continue           # If left pointer <= right pointer, continue
  li t2, -1                      # Key not found
  j done

continue:
  add t3, t0, t1                 # Calculate middle index
  srai t3, t3, 1                 # t3 = (t0 + t1) / 2
  li t4, 10                      # Search key
  blt t4, t3, adjust_left        # If key < middle element, adjust left pointer
  bge t4, t3, adjust_right       # If key > middle element, adjust right pointer
  j found                        # Key found at middle index

adjust_left:
  addi t1, t3, -1                # Adjust right pointer
  j loop

adjust_right:
  addi t0, t3, 1                 # Adjust left pointer
  j loop

found:
  mv t2, t3                      # Key found at index t3

done:
  # End the program by entering an infinite loop
  ebreak