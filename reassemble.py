import os
import glob

def reassemble_code(option, project_name):
    
    output_name = project_name + "_reassembled" + ".s"

    if option == 'sample':
        directory = "Sample_Assembly_Codes"
    elif option == 'code':
        directory = "User_Codes"
    else:
        raise ValueError("Options are: sample, code")

    input_file = list(glob.iglob(os.path.join("Software", directory, project_name, '*' + ".s")))[0]
    output_file = os.path.join("Software", directory, project_name, output_name)

    flag_addition_with_one = False
    flag_branch_with_addition_rd = False
    flag_addition_with_zero_reg = False

    m_extension = False

    count_addition_with_one = 0
    count_branch_with_addition_rd = 0
    count_addition_with_zero_reg = 0

    add_rd_register = ""
    previous_instruction = ""

    lines_without_flag = []

    with open(input_file, "r") as file:
        lines = file.readlines()

    for line in lines:
        line = line.strip()
        #instruction, *arguments = line.strip().split()

        # Skip lines starting with # (commented lines of assembly code)
        if line.startswith("#") or line.startswith("."):
            continue

        # Check if the previous instruction is an addition instruction
        if previous_instruction.startswith("add") or previous_instruction.startswith("addi"):
            # Check if the current line is a branch instruction
            if line.startswith("blt") or line.startswith("beq") or line.startswith("bne")  or line.startswith("bge")  or line.startswith("bltu") or line.startswith("bgeu"):
                tokens = line.split()
                rs1_register = tokens[1]
                rs2_register = tokens[2]
                # Check if the branch instruction uses the destination register of the preceding addition
                if rs1_register == add_rd_register or rs2_register == add_rd_register:
                    flag_branch_with_addition_rd = True
                    count_branch_with_addition_rd += 1

        # Check if the line is an addition instruction
        if line.startswith("add") or line.startswith("addi"):
            tokens = line.split()
            instruction_type = tokens[0]
            rd_register = tokens[1]
            # Check if the addition instruction has an immediate value of '1'
            if instruction_type == "addi" and tokens[3] == "1":
                flag_addition_with_one = True
                count_addition_with_one += 1
            # Check if the addition instruction has x0 (zero) register or sp (stack pointer) arg
            if line.startswith("add") or line.startswith("addi"):
                instruction, *arguments = line.split(",")
                if any(arg.strip() == "x0" for arg in arguments) or any(arg.strip() == "sp" for arg in arguments):
                    flag_addition_with_zero_reg = True
                    count_addition_with_zero_reg += 1
            add_rd_register = rd_register

        # Add line to array if it does not raise any flag
        if line.startswith("mul") or line.startswith("mulh") or line.startswith("mulhu") or line.startswith("mulhsu") or line.startswith("div") or line.startswith("divu") or line.startswith("rem") or line.startswith("remu"):
            m_extension = True
        else:
            m_extension = False
        if not flag_addition_with_one and not flag_branch_with_addition_rd and not flag_addition_with_zero_reg and (line.startswith("add") or line.startswith("addi") or m_extension):
            lines_without_flag.append(line)

        # Reset flags and counters for the next line
        flag_addition_with_one = False
        flag_branch_with_addition_rd = False
        flag_addition_with_zero_reg = False
        count_addition_with_one = 0
        count_branch_with_addition_rd = 0
        count_addition_with_zero_reg = 0

        previous_instruction = line

    if flag_branch_with_addition_rd:
        print("Flag raised! Branch instruction uses the destination register of a preceding addition.")
        print("Count of branch instructions with preceding addition rd register: " + str(count_branch_with_addition_rd) + "\n")
    else:
        print("Flag not raised. No branch instruction found with the destination register of a preceding addition.")

    if flag_addition_with_one:
        print("Flag raised! Addition instruction with immediate value '1' found.")
        print("Count of addition instructions with immediate value '1': " + str(count_addition_with_one) + "\n")

    if flag_addition_with_zero_reg:
        print("Flag raised! Addition instruction with zero register found.")
        print("Count of addition instructions with zero register: " + str(count_addition_with_zero_reg) + "\n")

    if lines_without_flag:
        print("Lines without raising any flag:")
        for line in lines_without_flag:
            print(line)
    else:
        print("All lines raised at least one flag.")

    with open(input_file, "r") as code:
        lines = code.readlines()
    # Search for the specific code lines and update the content
    updated_lines = []
    for i in range(len(lines)):
        line = lines[i].strip()
        updated_lines.append(line)
        if line in lines_without_flag:
            if i > 0:
                updated_lines[i - 1] += "\ncsrrw   set"
            if i < len(lines) - 1:
                updated_lines[i] += "\ncsrrw   reset"

    # Write the updated content to the output file
    with open(output_file, "w") as updated_code:
        updated_code.writelines('\n'.join(updated_lines))