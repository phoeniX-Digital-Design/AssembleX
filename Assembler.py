INSTRUCTIONS = {
    # R-Type Instructions
    "add": {"opcode": "0110011", "funct3": "000", "funct7": "0000000"},
    "sub": {"opcode": "0110011", "funct3": "000", "funct7": "0100000"},
    "and": {"opcode": "0110011", "funct3": "111", "funct7": "0000000"},
    "or":  {"opcode": "0110011", "funct3": "110", "funct7": "0000000"},
    "xor": {"opcode": "0110011", "funct3": "100", "funct7": "0000000"},
    "sll": {"opcode": "0110011", "funct3": "001", "funct7": "0000000"},

    # I-Type Instructions
    "addi": {"opcode": "0010011", "funct3": "000"},
    "ori" :  {"opcode": "0010011", "funct3": "110"},
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

def assemble(instruction, registers):
    opcode = INSTRUCTIONS[instruction]["opcode"]
    funct3 = INSTRUCTIONS[instruction].get("funct3", "")
    funct7 = INSTRUCTIONS[instruction].get("funct7", "")

    if instruction in ["lui", "auipc"]:
        rd, imm = registers
        return f"{opcode}{imm:020b}{rd:05b}"
    elif instruction in ["jal"]:
        rd, imm = registers
        return f"{opcode}{imm:020b}{rd:05b}"
    elif instruction in ["jalr"]:
        rd, rs1, imm = registers
        return f"{opcode}{imm:012b}{rs1:05b}{rd:05b}"
    elif instruction in ["sw", "sb"]:
        rs2, imm, rs1 = registers
        return f"{opcode}{imm[0:7]}{rs1:05b}{rs2:05b}{imm[7:12]}{funct3}"
    else:
        rd, rs1, imm = registers
        return f"{opcode}{imm:012b}{rs1:05b}{rd:05b}{funct7}{funct3}"

# Example usage
instruction = "addi"
registers = (1, 2, 10)
print(assemble(instruction, registers))  # Output: 00100110001000010000000000001010