from tqdm import tqdm
from itertools import product
from collections.abc import Sequence

def combo(operand, registers):
    if operand <=3 and operand >=0:
        return operand
    elif operand == 4 :
        return registers["A"]
    elif operand == 5 :
        return registers["B"]
    elif operand == 6 :
        return registers["C"]
    elif operand == 7 :
        print("Invalid Program")
        return None

def adv(registers,operand):
    combo_value = combo(operand, registers)
    registers["A"] = int(registers["A"]/(2**combo_value))
    return registers

def bxl(registers, operand):
    #Bitwise xor
    registers["B"] = registers["B"] ^ operand
    return registers

def bst(registers, operand):
    registers["B"] = combo(operand, registers)%8
    return registers    

def jnz(registers,operand):
    if registers["A"] != 0:
        return operand
    else:
        return None


def bxc(registers, operand):
    registers["B"] = registers["B"] ^ registers["C"]
    return registers

def out(registers,operand):
    return combo(operand, registers)%8

def bdv(registers, operand):
    registers["B"] = int(registers["A"]/(2**combo(operand, registers)))
    return registers

def cdv(registers, operand):
    registers["C"] = int(registers["A"]/(2**combo(operand, registers)))
    return registers


def opdecode(opcode):
    if opcode == 0:
        return adv
    elif opcode == 1:
        return bxl
    elif opcode == 2:
        return bst
    elif opcode == 3:
        return jnz
    elif opcode == 4:
        return bxc
    elif opcode == 5:
        return out
    elif opcode == 6:
        return bdv
    elif opcode == 7:
        return cdv
    


def main():

    with open('./Day17/file.txt') as f:
        lines = f.readlines()



    registers = {"A":0,"B":0,"C":0}
    registers["A"] = int(lines[0].split(": ")[1].strip('\n'))
    registers["B"] = int(lines[1].split(": ")[1].strip('\n'))
    registers["C"] = int(lines[2].split(": ")[1].strip('\n'))


    print(registers)
    op_str = lines[4].split(": ")[1]
    
    opcodes = []
    for op in op_str.split(","):
        opcodes.append(int(op))
    output = []
    inst_pointer = 0
    jmp = None
    while inst_pointer < len(opcodes):
        opcode = opcodes[inst_pointer]
        operand = opcodes[inst_pointer+1]
        if opcode == 3:
            jmp = opdecode(opcode)(registers,operand)
            if jmp != None:
                inst_pointer = jmp
        elif opcode == 5:
            val = opdecode(opcode)(registers,operand)
            output.append(val)
        else:
            registers = opdecode(opcode)(registers,operand)
        if jmp == None:
            inst_pointer += 2
        else:
            inst_pointer = jmp
            jmp = None        

    print("Answer to part 1: ",output)
    print(output == opcodes)
    #Part2

    output = []

    registers = {"A":0,"B":0,"C":0}

    #Find A doing iterations of the program in reverse that gives the output from the end
    target_output = opcodes[-1]
    

if __name__=="__main__":
    main()