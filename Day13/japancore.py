from collections import deque
from fractions import Fraction

def find_price(machine, costA=3, costB=1):
    price_x, price_y = machine["Prize"]
    
    moveXA, moveYA = machine["A"]
    moveXB, moveYB = machine["B"]

    moveXA, moveYA = int(moveXA), int(moveYA)
    moveXB, moveYB = int(moveXB), int(moveYB)

    if costA > costB:
        moveXB = int(costA/costB) * moveXB
        moveYB = int(costA/costB) * moveYB
    
    a = Fraction(price_x - Fraction(moveXB, moveYB) * price_y, moveXA - Fraction(moveXB, moveYB) * moveYA)
    b = Fraction(price_x - Fraction(moveXA, moveYA) * price_y, moveXB - Fraction(moveXA, moveYA) * moveYB)

    if int(b * int(costA/costB)) != b * int(costA/costB) or a > 100 or b > 100:
        print(b * int(costA/costB), a)
        return 0 

    return int(a * costA + b * costA)

def find_price_hardcore(machine, costA=3, costB=1):
    price_x, price_y = machine["Prize"]
    price_x, price_y = price_x+10000000000000, price_y+10000000000000
    moveXA, moveYA = machine["A"]
    moveXB, moveYB = machine["B"]

    moveXA, moveYA = int(moveXA), int(moveYA)
    moveXB, moveYB = int(moveXB), int(moveYB)

    if costA > costB:
        moveXB = int(costA/costB) * moveXB
        moveYB = int(costA/costB) * moveYB
    
    a = Fraction(price_x - Fraction(moveXB, moveYB) * price_y, moveXA - Fraction(moveXB, moveYB) * moveYA)
    b = Fraction(price_x - Fraction(moveXA, moveYA) * price_y, moveXB - Fraction(moveXA, moveYA) * moveYB)

    if int(b * int(costA/costB)) != b * int(costA/costB):
        print(b * int(costA/costB), a)
        return 0 

    return int(a * costA + b * costA)


def main():
    with open('./Day13/file.txt') as f:
        file = f.readlines()
    
    machines = []
    for line in range(0, len(file), 4):
        machine_dict = {"A": 0, "B": 0, "Prize": 0}
        for i in range(3):
            file[line + i] = file[line + i].strip('\n')
            if i == 0:
                machine_dict["A"] = (int(file[line + i].split("+")[1].split(",")[0]), file[line + i].split(",")[1].split("+")[1])
            elif i == 1:
                machine_dict["B"] = (int(file[line + i].split("+")[1].split(",")[0]), file[line + i].split(",")[1].split("+")[1])
            elif i == 2:
                machine_dict["Prize"] = (int(file[line + i].split('=')[1].split(",")[0]), int(file[line + i].split(",")[1].split('=')[1]))
        machines.append(machine_dict)

    sum = 0
    sum2 =0
    for machine in machines:  
        sum += find_price(machine)
        sum2+= find_price_hardcore(machine)
    print("Answer to part1: ", sum)
    print("Answer to part2: ", sum2)

if __name__ == '__main__':
    main()
