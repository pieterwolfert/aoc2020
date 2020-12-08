#!/env/user/bin python3



def main():
    with open('input.txt') as f:
        instructions = [i.strip().split(' ') for i in f.readlines()]
    nop_jump = [ind for ind, x in enumerate(instructions) if 'nop' in x or 'jmp' in x]
    for item in nop_jump:
        lcop = [i.copy() for i in instructions]
        if 'jmp' in lcop[item][0]:
            lcop[item][0] = 'nop'
        else:
            lcop[item][0] = 'jmp'
        acc, loop = checkprogram(lcop)
        if not loop:
            print(acc)

def checkprogram(instructions):
    indices = []
    step = 0
    acc = 0
    while step not in indices:
        if step >= len(instructions):
            return acc, False
        indices.append(step)
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
    main()


