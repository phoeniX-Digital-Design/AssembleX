from convert import AssemblyConverter as AC
import re

# instantiate object, by default outputs to a file in nibbles, not in hexademicals
convert = AC(output_mode = 'f', nibble_mode = True, hex_mode = False)

import re

def read_file(file_path):
    with open(file_path, 'r') as file:
        file_data = file.read()
    return file_data

def format_assembly_code(assembly_code):
    # Remove tabs and extra spaces
    assembly_code = re.sub(r'\t+', '', assembly_code)
    assembly_code = re.sub(r' {2,}', ' ', assembly_code)

    # Remove commas and add space between parameters
    assembly_code = re.sub(r',', ' ', assembly_code)
    assembly_code = re.sub(r'(\w+)([^\w\s])', r'\1 \2', assembly_code)
    assembly_code = re.sub(r'([^\w\s])(\w+)', r'\1 \2', assembly_code)

    return assembly_code

# Example usage
file_path = 'fibonacci.s'
file_contents = read_file(file_path)
formatted_code = format_assembly_code(file_contents)
print(formatted_code)

# Convert a string of assembly to binary file
cnv_str = '''sw a5 -24(s0)'''
convert(cnv_str, "New_AssembleX/result.txt")