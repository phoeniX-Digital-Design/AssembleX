from assembler_src.convert import AssemblyConverter as AC
import os
import sys
import glob

testbench_file = "phoeniX_Testbench.v"
option = sys.argv[1]
project_name = sys.argv[2]
output_name = project_name + "_firmware"

if option == 'sample':
    directory = "Sample_Assembly_Codes"
elif option == 'code':
    directory = "User_Codes"
else:
    raise ValueError("Options are: sample, code")

file_path = "assembler_src/" + output_name + ".txt"
print ("file path = " + file_path)

# instantiate object, by default outputs to a file in nibbles, not in hexademicals
convert = AC(output_mode = 'f', nibble_mode = True, hex_mode = False)
input_file  = list(glob.iglob(os.path.join("Software", directory, project_name, '*' + ".s")))[0]
output_file = os.path.join("Software", directory, project_name, output_name)

# Convert a whole .s file to text file
convert(input_file, file_path)
def remove_spaces_in_lines(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    lines = [line.replace('\t', '') for line in lines]
    with open(file_path, 'w') as file:
        file.writelines(lines)
remove_spaces_in_lines(file_path)

def binary_to_hex(binary_string):
    decimal_value = int(binary_string, 2)
    hex_string = hex(decimal_value)[2:].zfill(8)
    return hex_string

def convert_lines_to_hex(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    hex_lines = [binary_to_hex(line.strip()) for line in lines]
    with open(file_path, 'w') as file:
        file.write('\n'.join(hex_lines))
convert_lines_to_hex(file_path)

def change_file_format(file_path, new_format):
    directory, base_name = os.path.split(file_path)
    name, old_format = os.path.splitext(base_name)
    new_file_path = os.path.join(directory, name + new_format)
    os.rename(file_path, new_file_path)
    print(f"File renamed: {new_file_path}")

new_format = '.hex'
change_file_format(file_path, new_format)

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

# OS : cmd commands to execute Verilog simulations:
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