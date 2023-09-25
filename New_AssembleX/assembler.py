from convert import AssemblyConverter as AC
# instantiate object, by default outputs to a file in nibbles, not in hexademicals
convert = AC(output_mode = 'f', nibble_mode = True, hex_mode = False)

# Convert a whole .s file to text file
# convert("fibonacci.s", "result.txt")

# Convert a string of assembly to binary file
cnv_str = "add x1 x0 x0\nadd x2 x0 x1"
convert(cnv_str, "New_AssembleX/result.txt")