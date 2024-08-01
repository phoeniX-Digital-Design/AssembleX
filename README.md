![License](https://img.shields.io/github/license/phoeniX-Digital-Design/AssembleX?color=dark-green)
![Test](https://img.shields.io/badge/tests-passed-dark_green)
![RV32](https://img.shields.io/badge/integration_with_phoeniX-IM-blue)

AssembleX V3.0
===============

<div align="justify">

This repository contains source codes of `AssembleX`, the assembly code executant software for the [phoeniX RISC-V processor](https://github.com/phoeniX-Digital-Design/phoeniX) which is implemented in Verilog, at Electronics Research Center of Iran University of Science and Technology. AssembleX is powered by [riscv-assembler](https://github.com/celebi-pkg/riscv-assembler) and [PQR5ASM](https://github.com/iammituraj/pqr5asm) open-source projects. Current version of AssembleX supports `RV32IM` extenstions of standard RISC-V ISA.

This repository contains an open source software under the [GNU V3.0 license](https://en.wikipedia.org/wiki/GNU_General_Public_License) and is free to use.

- Contact Us: phoeniX.Digital.Electronics@gmail.com
- Iran University of Science and Technology - Electronics Research Center
- Digital Design Research Lab, SCaN Research Lab - Summer 2024

</div>

### How to use AssembleX
<div align="justify">

In order to run your own code on phoeniX, create a directory named to your project such as `/my_project` in `/Assembly_Codes/`. Put all your `user_code.s` files in my_project and run the following command from the main directory:
```
python AssembleX.py  my_project_directory/my_project.s
```
Provided that you name your project sub-directory correctly the AssembleX software will create `my_project_firmware.hex` and fed it directly to the testbench of phoeniX processor. After that, iverilog and GTKWave are used to compile the design and view the selected waveforms.

</div>

> [!NOTE]\
> AssembleX V3.0 is not integrated within the [phoeniX](https://github.com/phoeniX-Digital-Design/phoeniX) project repository yet. Currently phoeniX core is working with AssembleX V1.0 which is using the assistance of Venus Simulator VS code extension. **phoeniX** RISC-V processor will be empowered by **AssembleX V3.0** in the upcoming updates very soon!


> [!NOTE]\
> Permission to use, copy, modify, and/or distribute this software for any purpose with or without fee is hereby granted, provided that the above copyright notice and this permission notice appear in all copies.

 Copyright 2024 Iran University of Science and Technology. <phoenix.digital.electronics@gmail.com>
