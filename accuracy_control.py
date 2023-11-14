import re

def accuracy_control(file_path):
    set_lines = []
    reset_lines = []
    updated_lines = []
    replaced_count = 0

    with open(file_path, 'r') as file:
        lines = file.readlines()

    for i, line in enumerate(lines):
        tokens = re.findall(r'\S+', line)  # Split the line into tokens using regex
        if len(tokens) >= 2:
            if tokens[0] == 'csrrw':
                if tokens[1] == 'set':
                    set_lines.append(line.strip())
                    updated_lines.append(line)  # Preserve 'csrrw set' line
                    
                elif tokens[1] == 'reset':
                    reset_lines.append(line.strip())
                    prev_instruction = re.findall(r'\S+', lines[i-1])[-1] if i > 0 else None
                    next_instruction = re.findall(r'\S+', lines[i+1])[0] if i < len(lines) - 1 else None
                    if prev_instruction and prev_instruction.startswith(('add', 'addi')) or next_instruction and next_instruction.startswith(('add', 'addi')):
                        updated_lines.append('csrrw\tx0,\t\t0x801,\tx0\n')
                        replaced_count += 1
                    else:
                        updated_lines.append(line)
            else:
                updated_lines.append(line)
        else:
            updated_lines.append(line)

    with open(file_path, 'w') as file:
        file.writelines(updated_lines)

    return set_lines, reset_lines, replaced_count

# Usage example:
file_path = 'Software/Sample_Assembly_Codes/sum1to100/sum1to100_reassembled.s'
set_lines, reset_lines, replaced_count = accuracy_control(file_path)

print("Lines with 'csrrw set':")
for line in set_lines:
    print(line)

print("Lines with 'csrrw reset':")
for line in reset_lines:
    print(line)

print("Replaced", replaced_count, "lines with 'csrrw reset'.")