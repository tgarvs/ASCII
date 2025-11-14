
import time
import sys
import random
import threading
import shutil
import os
import queue
import tty, sys, termios


FRAMERATE = 1/24
cols, rows = os.get_terminal_size()


class Drop :
    def __init__(self) :
        self.drop = "." 
        self.x = random.randrange(0, cols, 1)
        self.y = random.randrange(0, rows, 1)
        self.y_speed = random.randrange(1, 3, 1)
        self.x_speed = 1


    def move(self, buff) :
        prev_y = self.y - self.y_speed
        prev_x = self.x - self.x_speed


        if(self.y < len(buff) - self.y_speed) :
            self.y = self.y + self.y_speed
        else :
            self.y = 0
        
        if(self.x < len(buff[0]) - self.x_speed) :
            self.x = self.x + self.x_speed
        else :
            self.x = 0


        buff[self.y][self.x] = self.drop
        buff[prev_y][prev_x] = self.drop

    
class Guy :
    def __init__(self) :
        self.x = cols//2
        self.y = rows-1
        self.moveAmt = 3
    
    def display(self, buff) :
        buff[self.y][self.x] = "&"

    def move(self, c: str) :
        if c == 'd' :
            if self.x < cols - self.moveAmt :
                self.x = self.x + self.moveAmt
            else :
                self.x = 1
        
        if c == 'a' :
            if self.x > 0 + self.moveAmt :
                self.x = self.x - self.moveAmt
            else :
                self.x = cols - self.moveAmt





#Stole and modified this code from here: https://code.activestate.com/recipes/134892/
def listener(in_q):
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try :
        while True :
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
            if not ch :
                continue
            in_q.put(ch)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    
    


if __name__ == "__main__" :
    print('\x1b[?25l', end="") #hides cursor

    close_flag = False

    #wipe screen and set cursor to 0,0 and turn on bold
    sys.stdout.write("\x1b[2J\x1b[H")
    sys.stdout.write("\x1b[3;7h")
    sys.stdout.write("\x1b[1m")
    sys.stdout.flush()

    #make one instance of the drop
    instances = []
    for i in range(60) :
        instances.append(Drop())


    g = Guy()

    q = queue.Queue()
    th = threading.Thread(target=listener, args=(q,), daemon=True)
    th.start()
    frame_buffer = [[" "]*cols for _ in range(rows)] #needs space to actually clear it
 


    while True:

        #clear render buffer
        for y in range(len(frame_buffer)) :
            for x in range(len(frame_buffer[y])) :
                frame_buffer[y][x] = " "


        #put all elements of new frame into a frame buffer
        for i in instances :
            i.move(frame_buffer)
        g.display(frame_buffer)


        #print the buffer frame
        for y in range(len(frame_buffer)) :
            for x in range(len(frame_buffer[y])) :
                sys.stdout.write(f"\x1b[{y};{x}H" + frame_buffer[y][x])

        #where to write stuff directly to screen
        sys.stdout.write("\x1b[H" + f"Length of Instances : {len(instances)}")
        if th.is_alive :
            sys.stdout.write("\x1b[3;0H" + "Thread still running")
        
        #check for user input events
        if not q.empty() :
            sys.stdout.write("\x1b[6;0H" + "Something in Queue")
            k = q.get()
            if k == 'q' :
                close_flag = True
            
            elif k == 'd' or k == 'a' :
                g.move(k)


        #push out frame and pause for a frame
        sys.stdout.flush()
        time.sleep(FRAMERATE)
        
        if(close_flag == True) :
            break
    

    
    



                






    





