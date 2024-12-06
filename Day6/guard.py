import polars as pl
import numpy as np

class guard():
    def __init__(self,map):
        self.map = map.copy()
        self.initialmap = map.copy()
        self.direction = "up"
        self.posx, self.posy = self.find_start(map)
        self.previouspos = (self.posx,self.posy)
        self.initialpath = [(self.posx,self.posy,self.direction)]
        self.currentpath = [(self.posx,self.posy,self.direction)]
        self.loop_list = []
        self.walk()
        

    def find_loop(self, map):
        #Find all possible way that the guard ends up in a loop
        self.map = map.copy()
        num_loops = 0
        candidates = []
        for k in range(len(self.initialpath)):
            x,y,_ = self.initialpath[k]
            candidates.append((x,y)) 
        for i in range(1,len(candidates)):
                    self.map = self.initialmap.copy()
                    self.posx, self.posy,self.direction = self.initialpath[i-1]
                    self.currentpath = self.initialpath[:i].copy()
                    try:
                        if self.map[candidates[i][0]][0][candidates[i][1]] != "#" and self.map[candidates[i][0]][0][candidates[i][1]] != "^":
                            self.map[candidates[i][0]][0] = self.map[candidates[i][0]][0][:candidates[i][1]]+"O"+self.map[candidates[i][0]][0][candidates[i][1]+1:]
                            if (candidates[i][0], candidates[i][1]) not in self.loop_list:
                                if self.walk_in_loops():
                                    self.loop_list.append((candidates[i][0], candidates[i][1]))
                                    num_loops += 1
                    except IndexError:
                        pass

        return num_loops

    def find_start(self, map):
        for i in range(len(map)):
            for j in range(len(map[i][0])):
                if map[i][0][j] == "^":
                    return i,j
        return 0,0
    
    def walk_in_loops(self):
        while True:
            try:
                if self.check_direction_loop():
                    return True
                if self.check_direction():

                    self.previouspos = (self.posx,self.posy)
                    if self.direction == "up":
                        #self.map[self.posx][0] = self.map[self.posx][0][:self.posy]+"X"+self.map[self.posx][0][self.posy+1:]
                        self.posx -= 1
                    elif self.direction == "down":
                        #self.map[self.posx][0] = self.map[self.posx][0][:self.posy]+"X"+self.map[self.posx][0][self.posy+1:]
                        self.posx += 1
                    elif self.direction == "left":
                        #self.map[self.posx][0] = self.map[self.posx][0][:self.posy]+"X"+self.map[self.posx][0][self.posy+1:]
                        self.posy -= 1
                    elif self.direction == "right":
                        #self.map[self.posx][0] = self.map[self.posx][0][:self.posy]+"X"+self.map[self.posx][0][self.posy+1:]
                        self.posy += 1

                    self.currentpath.append((self.posx,self.posy,self.direction))
            except IndexError:
                return False

    def walk(self):
        while True:
            try:
                if self.check_direction():
                    self.map[self.posx][0] = self.map[self.posx][0][:self.posy]+"X"+self.map[self.posx][0][self.posy+1:]
                    if self.direction == "up":
                        self.posx -= 1
                    elif self.direction == "down":
                        self.posx += 1
                    elif self.direction == "left":
                        self.posy -= 1
                    elif self.direction == "right":
                        self.posy += 1
                    self.initialpath.append((self.posx,self.posy,self.direction))
                    self.map[self.posx][0] = self.map[self.posx][0][:self.posy]+"^"+self.map[self.posx][0][self.posy+1:]
            except IndexError:
                self.map[self.posx][0] = self.map[self.posx][0][:self.posy]+"X"+self.map[self.posx][0][self.posy+1:]
                return self.map

    def check_direction_loop(self):
        if len(self.currentpath) >3:
            try:
                for idx in range(len(self.currentpath[:-2]) ):
                    x,y,_ = self.currentpath[idx]
                    x1,y1,_ = self.currentpath[idx+1]
                    if [(x,y),(x1,y1)] == [self.previouspos, (self.posx, self.posy)]:
                        return True
            except ValueError:
                pass    
        return False
        
    
    def check_direction(self):
        if self.direction == "up":
            if self.map[self.posx-1][0][self.posy] == "#" or self.map[self.posx-1][0][self.posy] == "O":
                self.direction = "right"
                return False
        elif self.direction == "right":
            if self.map[self.posx][0][self.posy+1] == "#" or self.map[self.posx][0][self.posy+1] == "O":
                self.direction = "down"
                return False
        elif self.direction == "down":
            if self.map[self.posx+1][0][self.posy] == "#" or self.map[self.posx+1][0][self.posy] == "O":
                self.direction = "left"
                return False
        elif self.direction == "left":
            if self.map[self.posx][0][self.posy-1] == "#" or self.map[self.posx][0][self.posy-1] == "O":
                self.direction = "up"
                return False
        return True
    
def main():
    map = pl.read_csv("./Day6/file.txt", has_header=False).to_numpy()
    #print(map[1][0][0])
    gd = guard(map.copy())
    sum = 0
    for i in range(len(gd.map)):
        for j in range(len(gd.map[i][0])):
            if gd.map[i][0][j] == "X":
                sum += 1

    print("Answer to part 1:", sum)
    print("Answer to part 2:", gd.find_loop(map))

if __name__ == "__main__":
    main()