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
            idx = int(data_size[i])+int(empty_space[i-1])
            
        indexes.append(idx)
    indexes.append(int(empty_space[-1]))
        #print(indexes)
    indexes = np.cumsum(indexes)
    #print(data_size)
    #print(empty_space)
    #print(indexes)
    
    for i in range(len(empty_space)):
        for j in range(int(empty_space[i])):
            #print(indexes[i])
            out.insert(indexes[i]+j, out[-1])
            out.pop()
    return out

def reallocate_without_segmentation(line):
    len_line = len(line)
    data_size = [line[f] for f in range(0, len_line, 2)]
    empty_space = [line[f] for f in range(1, len_line, 2)]
    empty_space_int = [int(f) for f in empty_space]
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
        idx = int(data_size[i])
        indexes.append(idx)
    indexes.append(int(empty_space[-1]))
    indexes = np.cumsum(indexes).tolist()
    data_size_copy = data_size.copy()
    #print(indexes)
    #print(data_size)
    #print(empty_space)
    #print(indexes)
    index_to_skip=0
    num_added=0
    num_deleted=0
    while len(data_size_copy)>0:

        for j in range(len(empty_space)):
            if int(empty_space[j]) >= int(data_size[-1]):
                #print(indexes[i])
                temp_data_size = int(data_size[-1])
                for _ in range(int(empty_space[j])):
                    if data_size[-1] == '1':
                        #convert out to dict
                        out_dict = dict(enumerate(out))
                        #If multiple occurrences of indextoskip-1 in out then break because we have found the cycle
                        if(list(out_dict.values()).count(out[-index_to_skip-1]) > 1):
                            return out
                    print("Empty space: ",j+1, "of size ", empty_space[j], "matches")
                    out.insert(indexes[j], out[-index_to_skip-1])
                    out.pop(len(out)-1-index_to_skip)
                    print(out)
                    empty_space[j] = str(int(empty_space[j])-1)
                    empty_space_int[j] -= 1
                    for l in range(j,len(empty_space)):
                        indexes[l] += 1
                    print("Empty space: ", empty_space)
                    temp_data_size -= 1
                    print(temp_data_size)
                    if temp_data_size == 0:
                        size = data_size.pop()
                        data_size.insert(j+num_added+num_deleted,size)
                        num_added += 1
                        print(data_size)
                        data_size_copy.pop()
                        break

            if empty_space[j] == '0':
                num_deleted+=1
                indexes.pop(j)
                empty_space.pop(j)
                empty_space_int.pop(j)
                break          
        try:
            if int(data_size[-1]) > max(empty_space_int):
                index_to_skip += int(data_size[-1])
                data_size.pop()
                data_size_copy.pop()
            print('Data_size', data_size)
            print('Data copy', data_size_copy)
        except:
            return out
    print(out)
    return out


def reallocate2(line):
    len_line = len(line)
    data_size = [line[f] for f in range(0, len_line, 2)]
    empty_space = [line[f] for f in range(1, len_line, 2)]
    out_line = []
    empty_space = empty_space
    empty =[]

    curr_id = 0
    curr_pos = 0
    for i in range(len(line)):
        if i % 2:
            # si c'est un espace libre
            empty.append((curr_pos, int(line[i])))
        else:
            # si c'est un fichier
            out_line.append((curr_pos, int(line[i]), curr_id))
            curr_id += 1
        curr_pos += int(line[i])

    print("debug:" + str(out_line))
    for i in range(len(out_line)-1,0,-1):
        # print("debug:" + str(out_line))
        for j in range(len(empty)):
            if empty[j][1] >= out_line[i][1] and empty[j][0] < out_line[i][0]:
                out_line[i] = (empty[j][0], out_line[i][1], out_line[i][2])
                #order out_line by position
                empty[j] = (empty[j][0]+out_line[i][1], empty[j][1]-out_line[i][1])
                break
    return out_line

"""    indextoskip=0
    for i in range(len(data_size)):
        data_count = int(data_size[i])
        consecutive_dots = 0
        max_consecutive = 0
        # Count consecutive dots
        for j in range(len(out_line)):
            if out_line[j] == '.':
                consecutive_dots += 1
            else:
                max_consecutive = max(max_consecutive, consecutive_dots)
                consecutive_dots = 0
        max_consecutive = max(max_consecutive, consecutive_dots)
        if int(data_size[-1]) > max_consecutive:
        # Only replace if data_count is less than or equal to max consecutive dots
        if data_count <= max_consecutive:
            for _ in range(data_count):
                try:
                    idx = out_line.index('.')
                    out_line[idx] = out_line[-indextoskip-1]
                    out_line.pop()
                except ValueError:
                    print(out_line)
                    return out_line
        print(out_line)
    return out_line"""

def main():
    with open("./Day9/file.txt") as f:
        lines = f.readlines()

    reallocated = reallocate(lines[0])    
    sum = 0
    for i in range(len(reallocated)):
        sum += reallocated[i]*i
    print("Answer to part 1: ", sum)
    #Should get 6262891638328
    #Got        6264446295468
    reallocated2 = reallocate2(lines[0])
    sum2=0

    reallocated2.reverse()
    # print("RESULTAT=:" + str(reallocated2[:300]))
    for i in range(len(reallocated2)):
        for j in range(reallocated2[i][1]):
            sum2 += reallocated2[i][2]*(j+reallocated2[i][0])
    print("Answer to part 2: ", sum2)
if __name__ == "__main__":
    main()