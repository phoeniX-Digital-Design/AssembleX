# RV32I Assembler

# Instruction formats
R_FORMAT = 0
I_FORMAT = 1
S_FORMAT = 2
B_FORMAT = 3
U_FORMAT = 4
J_FORMAT = 5

# Register mappings
REGISTERS = {
    "zero": 0,  "ra": 1,  "sp" : 2,  "gp" : 3,  "tp": 4,  "t0": 5,  "t1": 6,  "t2": 7,
    "s0"  : 8,  "s1": 9,  "a0" : 10, "a1" : 11, "a2": 12, "a3": 13, "a4": 14, "a5": 15,
    "a6"  : 16, "a7": 17, "s2" : 18, "s3" : 19, "s4": 20, "s5": 21, "s6": 22, "s7": 23,
    "s8"  : 24, "s9": 25, "s10": 26, "s11": 27, "t3": 28, "t4": 29, "t5": 30, "t6": 31
}

# Opcode mappings
OPCODES = {
    "lui"  : 0b0110111, "auipc": 0b0010111, "jal" : 0b1101111, "jalr": 0b1100111,
    "beq"  : 0b1100011, "bne"  : 0b1100011, "blt" : 0b1100011, "bge" : 0b1100011,
    "bltu" : 0b1100011, "bgeu" : 0b1100011, "lb"  : 0b0000011, "lh"  : 0b0000011,
    "lw"   : 0b0000011, "lbu"  : 0b0000011, "lhu" : 0b0000011, "sb"  : 0b0100011,
    "sh"   : 0b0100011, "sw"   : 0b0100011, "addi": 0b0010011, "slti": 0b0010011,
    "sltiu": 0b0010011, "xori" : 0b0010011, "ori" : 0b0010011, "andi": 0b0010011,
    "slli" : 0b0010011, "srli" : 0b0010011, "srai": 0b0010011, "add" : 0b0110011,
    "sub"  : 0b0110011, "sll"  : 0b0110011, "slt" : 0b0110011, "sltu": 0b0110011,
    "xor"  : 0b0110011, "srl"  : 0b0110011, "sra" : 0b0110011, "or"  : 0b0110011,
    "and"  : 0b0110011
}

# Function mappings for R-format instructions
FUNCTIONS = {
    "add" : 0b0000000, "sub": 0b0100000, "sll": 0b0000001, "slt": 0b0000010,
    "sltu": 0b0000011, "xor": 0b0000100, "srl": 0b0000101, "sra": 0b0100101,
    "or"  : 0b0000110, "and": 0b0000111
}

def assemble(assembly_code):
    machine_code = []

    # Split the code into lines
    code_lines = assembly_code.split("\n")

    # Process each line of code
    for line in code_lines:
        line = line.strip()

        # Ignore empty lines and comments
        if not line or line.startswith("#") or line.startswith("."):
            continue

        # Split the line into tokens
        tokens = line.split()

        # Extract the instruction and its arguments
        instruction = tokens[0]
        args = tokens[1:]

        # Determine the instruction format
        if instruction in ["lui", "auipc", "jal"]:
            format_type = U_FORMAT
        elif instruction in ["jalr"]:
            format_type = I_FORMAT
        elif instruction in ["beq", "bne", "blt", "bge", "bltu", "bgeu"]:
            format_type = B_FORMAT
        elif instruction in ["lb", "lh", "lw", "lbu", "lhu", "sb", "sh", "sw","addi"]:
            format_type = I_FORMAT
        else:
            format_type = R_FORMAT

        # Encode the instruction based on the format
        if format_type == R_FORMAT:
            opcode = OPCODES[instruction]
            funct3 = 0b000
            funct7 = FUNCTIONS[instruction]
            rd = REGISTERS[args[0]]
            rs1 = REGISTERS[args[1]]
            rs2 = REGISTERS[args[2]]
            machine_code.append((funct7 << 25) | (rs2 << 20) | (rs1 << 15) | (funct3 << 12) | (rd << 7) | opcode)

        elif format_type == I_FORMAT:
            opcode = OPCODES[instruction]
            rd = REGISTERS[args[0]]
            rs1 = REGISTERS[args[1]]
            imm = int(args[2])
            machine_code.append((imm << 20) | (rs1 << 15) | (funct3 << 12) | (rd << 7) | opcode)

        elif format_type == S_FORMAT:
            opcode = OPCODES[instruction]
            imm = int(args[1])
            rs1 = REGISTERS[args[2]]
            rs2 = REGISTERS[args[0][args[0].index("(") + 1:-1]]
            machine_code.append((imm << 25) | (rs2 << 20) | (rs1 << 15) | (funct3 << 12) | opcode)

        elif format_type == B_FORMAT:
            opcode = OPCODES[instruction]
            funct3 = OPCODES[instruction]
            rs1 = REGISTERS[args[0]]
            rs2 = REGISTERS[args[1]]
            imm = int(args[2])
            offset = ((imm >> 11) & 1) << 12 | ((imm >> 1) & 0b11111110) << 5 | ((imm >> 5) & 0b1) << 11 | ((imm >> 12) & 0b1111) << 1
            machine_code.append((offset << 19) | (rs2 << 24) | (rs1 << 15) | (funct3 << 12) | opcode)

        elif format_type == U_FORMAT:
            opcode = OPCODES[instruction]
            rd = REGISTERS[args[0]]
            imm = int(args[1])
            machine_code.append((imm << 12) | (rd << 7) | opcode)

        elif format_type == J_FORMAT:
            opcode = OPCODES[instruction]
            rd = REGISTERS[args[0]]
            imm = int(args[1])
            offset = ((imm >> 19) & 1) << 20 | ((imm >> 0) & 0b1111111111) << 1 | ((imm >> 10) & 0b1) << 11 | ((imm >> 11) & 0b111111111) << 12
            machine_code.append((offset << 11) | (rd << 7) | opcode)

    return machine_code


# Example assembly code
assembly_code = """
    # Calculate the sum of two numbers
    addi t0, zero, 5
    addi t1, zero, 10
    add t2, t0, t1
    """

# Assemble the code
machine_code = assemble(assembly_code)

# Print the machine code
for instruction in machine_code:
    print(bin(instruction)[2:].zfill(32))