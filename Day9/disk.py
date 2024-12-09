import numpy as np

def reallocate(line):
    len_line = len(line)
    data_size = [line[f] for f in range(0, len_line, 2)]
    empty_space = [line[f] for f in range(1, len_line, 2)]
    out_line = []
    out = []
    for i in range(len(data_size)):
        try:
            out_line += [i]*int(data_size[i])
            out_line += ['.']*int(empty_space[i])
        except:
            break
    """for block in range(len(data_size),0,-1):
        for k in range(block):    
            for j in range(len(empty_space)):      
                    out_line.insert(int(empty_space[j]), k%10)
    """
    #print(out_line)
    indexes=[]
    for i in range(len(data_size)):
        out += [i]*int(data_size[i])
        if i == 0 or i == len(data_size)-1:
            idx = int(data_size[i])
        else:
            idx = int(data_size[i])+int(empty_space[i])
        indexes.append(idx)
        #print(indexes)
    indexes = np.cumsum(indexes)[:-1]
    #print(indexes)
    for i in range(len(data_size)):
        data_count = int(data_size[i])
        for _ in range(data_count):
            try:
                idx = out_line.index('.')
                out_line[idx] = out_line[-1]
                out_line.pop()
            except ValueError:
                return out_line
def main():
    with open("./Day9/file.txt") as f:
        lines = f.readlines()

    reallocated = reallocate(lines[0])    
    sum = 0
    for i in range(len(reallocated)):
        sum += reallocated[i]*i

    print("Answer to part 1: ", sum)


if __name__ == "__main__":
    main()