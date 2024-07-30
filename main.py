import  sys
from    variables          import   *
from    assembler          import   assembler
from    address_mapping    import   address_mapping
from    address_mapping    import   label_mapping
from    address_mapping    import   define_reset_address
from    data_conversion    import   binary_to_hex
from    data_conversion    import   ascii_to_hex

try:
    source_path = sys.argv[1]
    firmware_bin_path = sys.argv[1].rstrip('.s') + '_firmware.bin'
    firmware_hex_path = sys.argv[1].rstrip('.s') + '_firmware.hex'
except:
    print('INFO: No arguments/unsupported arguments\n')

try:
    source_file = open(source_path, "r")
    source_code_unformatted = source_file.read().splitlines()
    print("\nINFO: Source file opened successfully\n")
except:
    print("FATAL ERROR:  Unable to open source file\n")
    exit(1)

print('Assembly code pre-processing')
print('----------------------------')
source_code = []
for line in source_code_unformatted:
    instruction_format_space = " ".join(line.split())
    instruction_format_comments = " #".join(instruction_format_space.split('#', 2))
    instruction_format_leadspace = instruction_format_comments.lstrip()
    source_code.append(instruction_format_leadspace)

# Re-format immediate expressions
processed_code_1 = []
for line in source_code:
    arguments = line.split(',')
    try:
        if arguments[0][0] == '#':
            processed_code_1.append(line)
            continue
        elif arguments[0] == '.RESET_ADDRESS':
            processed_code_1.append(line)
            continue
    except:
        processed_code_1.append(line)
        continue
    # Check for 2 argument immediate expressions: 'x(y)' -> parse: 'y x'
    # Check for ASCII: char -> hex
    parse_ascii = [False]
    try:
        arg2wc = arguments[1]
        arg2wc = arg2wc.split('#', 2)
        len_arg2wc = len(arg2wc)
        arg2 = [arg2wc[0]]
        ascii_to_hex(arg2)
        arg2pp = arg2[0].replace(')', '(')
        arg2pp = "".join(arg2pp.split())
        arg2list = arg2pp.split('(')
        if len_arg2wc == 2:
            arguments[1] = ' ' + arg2list[1] + ', ' + arg2list[0] + ' ' + '#' + arg2wc[1]  # Modified expression
        else:  # No inline comment
            arguments[1] = ' ' + arg2list[1] + ', ' + arg2list[0]  # Modified expression
        processed_code_1.append(",".join(arguments))
    except:
        if parse_ascii[0]:
            if len_arg2wc == 2:
                arguments[1] = arg2[0] + ' ' + '#' + arg2wc[1]  # Modified expression
            else:
                arguments[1] = arg2[0]  # Modified expression
            processed_code_1.append(",".join(arguments))
        else:
            processed_code_1.append(line)
        continue

# Remove "," change "," -> " "
processed_code_2 = []
for line in processed_code_1:
    line = line.replace(',', ' ')
    processed_code_2.append(" ".join(line.split()))

lines_of_code = len(processed_code_2)
print('Lines of code pre-processed =', lines_of_code, '\n')

start_address = define_reset_address(processed_code_2[0])

for line in source_code:
    label_state = label_mapping(start_address, line, instruction_counter, 
                                expected_instructions_count, lable_counter, 
                                label_list, label_address_list)
address_mapping(lable_counter, label_list, label_address_list)

# Parser
print('')
print('Parser')
print('------')
pc[0] = start_address
for line in processed_code_2:
    instruction_sts = assembler(pc, line, line_number, error_flag, error_counter, bin_instruction)
    line_number = line_number + 1

# Summary
print('\nSummary')
print('-------')
if error_flag[0] == 0:
    print('- Lines of code (source)   = ', lines_of_code)
    print('- Assembled instructions   = ', instruction_counter[0])
    print('- Instructions with ERRORS = ', error_counter[0])
    binary_to_hex(bin_instruction, hex_instruction)
    try:
        # Binary text file write
        file = open(firmware_bin_path, "w")
        binary_data = bytearray()
        for line in bin_instruction:
            file.write(line + '\n')
            dbyte3 = line[0  :  8]
            dbyte2 = line[8  : 16]
            dbyte1 = line[16 : 24]
            dbyte0 = line[24 : 32]
            binary_data.append(int(dbyte3, 2))
            binary_data.append(int(dbyte2, 2))
            binary_data.append(int(dbyte1, 2))
            binary_data.append(int(dbyte0, 2))
        # Dump .bin file
        instr_totalsize_bytes = instruction_counter[0] * 4
        file.close()

        # Hex text file write
        file = open(firmware_hex_path, "w")
        for line in hex_instruction:
            file.write(line + '\n')
        print('\nSUCCESS: Successfully created FIRMWARE file')
        file.close()
    except:
        print('FATAL ERROR: Unable to create FIRMWARE file')
else:
    print('No. of lines of code parsed     = ', lines_of_code)
    print('No. of instructions parsed      = ', instruction_counter[0])
    print('No. of instructions with ERRORS = ', error_counter[0])
    print('\nFAIL:Failed to parse the assembly code due to errors')
    exit(2)