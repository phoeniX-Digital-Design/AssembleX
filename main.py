from reassemble import reassemble_code
import os
import sys

testbench_file = "phoeniX_Testbench.v"

# Reassemble code with approximate arithmetic:
option = sys.argv[1]
project_name = sys.argv[2]
output_file = project_name + "_firmware.hex"
reassemble_code(option, project_name)

# Change firmware in the testbench file
with open(testbench_file, 'r') as file:
    lines = file.readlines()
# Edit source files of testbench names
with open(testbench_file, 'w') as file:
    for line in lines:
        # Change instruction memory source file
        if line.startswith("\t`define FIRMWARE"):
            print("Line found!")
            # Modify the input file name
            output_file = output_file.replace("\\", "\\\\")
            modified_line = line.replace(line,'\t`define FIRMWARE '+ '"' + output_file + '"' +'\n' )
            file.write(modified_line)
        else:
            file.write(line)

# OS tasks: cmd commands to execute Verilog simulations:
os.system("iverilog -IModules -o phoeniX.vvp phoeniX_Testbench.v") 
os.system("vvp phoeniX.vvp") 
with open(testbench_file, 'w') as file:
    for line in lines:
        # Change testbench file
        if line.startswith("\t`define FIRMWARE"):
            print("Line found!")
            # Remove firmware file address
            modified_line = line.replace(line,'\t`define FIRMWARE\n')
            file.write(modified_line)
        else:
            file.write(line)
os.system("gtkwave phoeniX.gtkw") 