from convert import AssemblyConverter as AC
import re

# instantiate object, by default outputs to a file in nibbles, not in hexademicals
convert = AC(output_mode = 'f', nibble_mode = True, hex_mode = False)

# Convert a string of assembly to binary file
cnv_str = '''sw a5 -24(s0)'''
convert(cnv_str, "New_AssembleX/result.txt")

# Convert a whole .s file to text file
convert("test.s", "New_AssembleX/result.txt")