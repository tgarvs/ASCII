
import time
import sys
import random
import threading
import shutil
import os
import queue

#TODO: allow user input and resizing

class Drop :
    def __init__(self) :
        self.rows, self.cols = shutil.get_terminal_size()

        self.drop = "." 
        self.x = random.randrange(0, self.rows, 1)
        self.y = random.randrange(0, self.cols, 1)
        self.y_speed = random.randrange(1, 3, 1)
        self.start_time = time.time()
        self.speed = 0.0006


    def move(self) :
        time.sleep(self.speed) #speed at which it moves

        prev_y = self.y - self.y_speed - 0
        prev_x = self.x - 1

        sys.stdout.write(f"\x1b[{self.y};{self.x}H" + self.drop) #move down one line
        sys.stdout.write(f"\x1b[{prev_y};{prev_x}H" + self.drop) 
    
        if(self.y < self.cols) :
            self.y = self.y + self.y_speed
        else :
            self.y = 0
        
        if(self.x < self.rows) :
            self.x = self.x + 1
        else :
            self.x = 0


        
        
class Guy :
    def __init__(self) :
        self.x = 10
        self.y = 0
    
    def display(self) :
        sys.stdout.write(f"\x1b[{self.y};{self.x}H" + "&") 
        sys.stdout.flush()


    def move(self, c: str) :
        print("GUY MOVE CALLED")
        if c == 'd' :
            self.x = self.x + 10

    
def listener(in_q) :
    for line in sys.stdin :
        in_q.put(line.rstrip('\n'))

    


if __name__ == "__main__" :
    print('\x1b[?25l', end="") #hides cursor

    close_flag = False

    #wipe screen and set cursor to 0,0 
    sys.stdout.write("\x1b[2J\x1b[H")
    sys.stdout.write("\x1b[3;7h")
    sys.stdout.write("\x1b[1m")
    sys.stdout.flush()

    #make one instance of the drop
    instances = []
    for i in range (60) :
        instances.append(Drop())

    g = Guy()
    q = queue.Queue()
    th = threading.Thread(target=listener, args=(q,), daemon=True)
    th.start()

    while True:
        sys.stdout.write("\x1b[2J")

        g.display()

        while not q.empty() :
            i = q.get()
            g.move(i)

        # for i in (instances) :
        #     i.move()
        # sys.stdout.flush()

        if(close_flag == True) :
            break
    

    
    



                






    





