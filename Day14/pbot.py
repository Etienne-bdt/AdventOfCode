import numpy as np
from tqdm import tqdm
from math import floor

def predict_end(bots, time_of_end=100, width=101, height=103):
    new_posx = (bots[0] + time_of_end * bots[2]) % width
    new_posy = (bots[1] + time_of_end * bots[3]) % height
    return (new_posx, new_posy)

def main():
    width = 101
    height = 103
    with open('./Day14/file.txt') as f:
        lines = f.readlines()
        
    bots = []
    for bot in lines:
        bot = bot.strip('\n')
        posx = bot.split('=')[1].split(',')[0]
        posy = bot.split('=')[1].split(',')[1].split(' ')[0]
        vx = bot.split('v=')[1].split(',')[0]
        vy = bot.split('v=')[1].split(',')[1]
        bots.append([int(posx), int(posy), int(vx), int(vy)])

    final_pos = []
    quad = [0,0,0,0]
    for bot in bots:
        final_pos.append(predict_end(bot, width=width, height=height))
        if final_pos[-1][0] < floor(width/2) and final_pos[-1][1] < floor(height/2):
            quad[0] += 1
        elif final_pos[-1][0] < floor(width/2) and final_pos[-1][1] > floor(height/2):
            quad[1] += 1
        elif final_pos[-1][0] > floor(width/2) and final_pos[-1][1] < floor(height/2):
            quad[2] += 1
        elif final_pos[-1][0]> floor(width/2) and final_pos[-1][1] > floor(height/2):
            quad[3] += 1

    print('Answer to part 1 : ', np.prod(quad),'\n')

    # Part 2
    for time in tqdm(range(25000)):
        final_pos = []
        for bot in bots:
            final_pos.append(predict_end(bot, time_of_end=time, width=width, height=height))
        #Check if we have bots in width/2,0 and width/2-1,1 and width/2+1,1 and width/2,2
        for pos in final_pos:
            if (pos[0]-1, pos[1]+1) in final_pos and (pos[0]+1, pos[1]+1) in final_pos and (pos[0], pos[1]+2) in final_pos and (pos[0], pos[1]+1) in final_pos and (pos[0]-2, pos[1]+2) in final_pos and (pos[0]+2, pos[1]+2) in final_pos and (pos[0]-1, pos[1]+2) in final_pos and (pos[0]+1, pos[1]+2) in final_pos and (pos[0], pos[1]+2) in final_pos:
                print('Answer to part 2 : ', time)
                break

if __name__=='__main__':
    main()