from convert import AssemblyConverter as AC
import os

file_path = "assembler_src/result.txt"
# instantiate object, by default outputs to a file in nibbles, not in hexademicals
convert = AC(output_mode = 'f', nibble_mode = True, hex_mode = False)

# Convert a whole .s file to text file
convert("test.s", file_path)

def remove_spaces_in_lines(file_path):
    # Read the contents of the file
    with open(file_path, 'r') as file:
        lines = file.readlines()
    # Remove spaces in each line
    lines = [line.replace('\t', '') for line in lines]
    # Write the modified lines back to the file
    with open(file_path, 'w') as file:
        file.writelines(lines)
remove_spaces_in_lines(file_path)

def binary_to_hex(binary_string):
    decimal_value = int(binary_string, 2)
    hex_string = hex(decimal_value)[2:].zfill(8)
    return hex_string

def convert_lines_to_hex(file_path):
    # Read the contents of the file
    with open(file_path, 'r') as file:
        lines = file.readlines()
    # Convert each line to hex format
    hex_lines = [binary_to_hex(line.strip()) for line in lines]
    # Write the hex lines to a new file
    with open(file_path, 'w') as file:
        file.write('\n'.join(hex_lines))
convert_lines_to_hex(file_path)

def change_file_format(file_path, new_format):
    # Split the file path into directory and base name
    directory, base_name = os.path.split(file_path)
    # Split the base name into name and old format
    name, old_format = os.path.splitext(base_name)
    # Generate the new file path with the new format
    new_file_path = os.path.join(directory, name + new_format)
    # Rename the file
    os.rename(file_path, new_file_path)
    print(f"File renamed: {new_file_path}")

new_format = '.hex'
change_file_format(file_path, new_format)