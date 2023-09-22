INSTRUCTIONS = {
    # R-Type Instructions
    "add": {"opcode": "0110011", "funct3": "000", "funct7": "0000000"},
    "sub": {"opcode": "0110011", "funct3": "000", "funct7": "0100000"},
    "and": {"opcode": "0110011", "funct3": "111", "funct7": "0000000"},
    "or" : {"opcode": "0110011", "funct3": "110", "funct7": "0000000"},
    "xor": {"opcode": "0110011", "funct3": "100", "funct7": "0000000"},
    "sll": {"opcode": "0110011", "funct3": "001", "funct7": "0000000"},

    # I-Type Instructions
    "addi": {"opcode": "0010011", "funct3": "000"},
    "ori" : {"opcode": "0010011", "funct3": "110"},
    "andi": {"opcode": "0010011", "funct3": "111"},

    # U-Type Instructions
    "lui"  : {"opcode": "0110111"},
    "auipc": {"opcode": "0010111"},

    # S-Type Instructions
    "sw": {"opcode": "0100011", "funct3": "010"},
    "sb": {"opcode": "0100011", "funct3": "000"},

    # B-Type Instructions
    "beq": {"opcode": "1100011", "funct3": "000"},
    "bne": {"opcode": "1100011", "funct3": "001"},

    # J-Type Instructions
    "jal": {"opcode": "1101111"},

    # System Instructions
    "ecall": {"opcode": "1110011", "funct3": "000", "funct7": "0000000"},
}

REGISTERS = {
    "zero": 0,
    "ra": 1,
    "sp": 2,
    "gp": 3,
    "tp": 4,
    "t0": 5,
    "t1": 6,
    "t2": 7,
    "s0": 8,
    "s1": 9,
    "a0": 10,
    "a1": 11,
    "a2": 12,
    "a3": 13,
    "a4": 14,
    "a5": 15,
    "a6": 16,
    "a7": 17,
    "s2": 18,
    "s3": 19,
    "s4": 20,
    "s5": 21,
    "s6": 22,
    "s7": 23,
    "s8": 24,
    "s9": 25,
    "s10": 26,
    "s11": 27,
    "t3": 28,
    "t4": 29,
    "t5": 30,
    "t6": 31,
}

def determine_format_type(instruction):
    if instruction in ["add", "sub", "and", "or", "xor", "sll"]:
        return "R"
    elif instruction in ["addi", "ori", "andi"]:
        return "I"
    elif instruction in ["sw", "sb"]:
        return "S"
    elif instruction in ["beq", "bne"]:
        return "B"
    elif instruction in ["lui", "auipc"]:
        return "U"
    elif instruction == "jal":
        return "J"
    elif instruction == "ecall":
        return "System"
    else:
        raise ValueError("Invalid instruction")

def assemble_r_type(instruction, rd, rs1, rs2):
    opcode = INSTRUCTIONS[instruction]["opcode"]
    funct3 = INSTRUCTIONS[instruction]["funct3"]
    funct7 = INSTRUCTIONS[instruction]["funct7"]
    return f"{funct7}{rs2}{rs1}{funct3}{rd}{opcode}"

def assemble_i_type(instruction, rd, rs1, imm):
    opcode = INSTRUCTIONS[instruction]["opcode"]
    funct3 = INSTRUCTIONS[instruction]["funct3"]
    imm_bin = format(imm, '012b')
    return f"{imm_bin}{rs1}{funct3}{rd}{opcode}"

def assemble_s_type(instruction, rs1, rs2,):
    opcode = INSTRUCTIONS[instruction]["opcode"]
    funct3 = INSTRUCTIONS[instruction]["funct3"]
    funct7 = INSTRUCTIONS[instruction]["funct7"]