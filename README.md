AssembleX V2.0
===============

<div align="justify">

This repository contains complete source code of `AssembleX`, the assembly code executant for [phoeniX RISC-V processor](https://github.com/phoeniX-Digital-Design/phoeniX) written in Verilog, at Electronics Research Center of Iran University of Science and Technology. AssembleX is now working with the help of [riscv-assembler](https://github.com/celebi-pkg/riscv-assembler) software.

</div>

### Running Sample Codes
<div align="justify">

Before running the script, note that the assembly code must be saved in the project directory with the same name.
To run any of these sample projects simply run python `AssembleX.py sample` followed by the name of the project passed as a variable named project to the Python script.
The input command format for the terminal follows the structure illustrated below:
```
python AssembleX.py sample {project_name}
```
For example:
```
python AssembleX.py sample fibonacci
```
After execution of this script, firmware file will be generated and this final file can be directly fed to our Verilog testbench. AssembleX automatically runs the testbench and calls upon gtkwave to display the selected signals in the waveform viewer application, gtkwave.
</div>

### Running Your Own Code
<div align="justify">

In order to run your own code on phoeniX, create a directory named to your project such as `/my_project` in `/Software/User_Codes/`. Put all your ``user_code.s` files in my_project and run the following command from the main directory:
```
python AssembleX.py code my_project
```
Provided that you name your project sub-directory correctly the AssembleX software will create `my_project_firmware.hex` and fed it directly to the testbench of phoeniX processor. After that, iverilog and GTKWave are used to compile the design and view the selected waveforms.
</div>
