#!/env/user/bin python3

import time

def main():
    with open('input.txt') as f:
        instructions = [i.strip().split(' ') for i in f.readlines()]
    nop_jump = [ind for ind, x in enumerate(instructions) if 'nop' in x or 'jmp' in x]
    for item in nop_jump:
        loop = True
        if 'jmp' in instructions[item][0]:
            instructions[item][0] = 'nop'
            acc, loop = checkprogram(instructions)
            instructions[item][0] = 'jmp'
        else:
            instructions[item][0] = 'jmp'
            acc, loop = checkprogram(instructions)
            instructions[item][0] = 'nop'
        if not loop:
            print(acc)

def checkprogram(instructions):
    indices = set()
    step = 0
    acc = 0
    while step not in indices:
        indices.add(step)
        if step >= len(instructions):
            return acc, False
        if 'acc' in instructions[step]:
            acc += int(instructions[step][1])
            step += 1
        elif 'jmp' in instructions[step]:
            step += int(instructions[step][1])
        else:
            step += 1
    if step in indices:
        return acc, True
    return acc, False

if __name__=="__main__":
    t0 = time.time()
    main()
    t1 = time.time()
    print(t1-t0)


