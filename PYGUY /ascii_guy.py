
import time
import sys
import random
import threading
import os
import queue
from pynput.keyboard import Key, Listener
import tty, sys, termios
import curses


FRAMERATE = 1/32
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
        self.velX = 0
        self.velY = 0
        self.accX = 0
        self.accY = 0
        self.moveAmt = 1
        self.maxSpeed = 3
    
    def display(self, buff) :
        self.velX += self.accX
        
        if self.velX >= self.maxSpeed :
            self.velX = self.maxSpeed
        elif self.velX <= -self.maxSpeed :
            self.velX = -self.maxSpeed
        
        self.x += self.velX

        if self.x > len(buff[0]) - abs(self.velX) :
            self.x = 1 + abs(self.velX)
        elif self.x < abs(self.velX) :
            self.x = len(buff[0]) - abs(self.velX)

        buff[self.y][self.x] = "&"


    def move(self, c: str, buff) :
        if c == 'd' :
            self.accX += self.moveAmt
        
        elif c == 'a' :
                self.accX -= self.moveAmt



    def halt(self) :
        self.accX = 0
        while self.velX != 0 :
            if self.velX >= 1 :
                self.velX -= 1
            else :
                self.velX += 1




def main(stdscr):

    close_flag = False
    curses.curs_set(0)      # hide cursor
    stdscr.nodelay(True)    # non-blocking getch
    stdscr.keypad(True)     # enable arrow keys, etc.


    #wipe screen and set cursor to 0,0 and turn on bold
    sys.stdout.write("\x1b[2J\x1b[H")
    sys.stdout.write("\x1b[3;7h")
    sys.stdout.write("\x1b[1m")
    print('\x1b[?25l', end="") #hides cursor
    sys.stdout.flush()

    #make one instance of the drop
    instances = []
    for i in range(60) :
        instances.append(Drop())


    g = Guy()
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


        #HUD
        L = f"Length of Instances : {len(instances)}"
        for s, l in zip(L, range(len(L))) :
            frame_buffer[1][l+3] = s

        V = f"Loc : {g.x}   Vel : {g.velX}    Acc : {g.accX}"
        for s, l in zip(V, range(len(V))) :
            frame_buffer[4][l+3] = s




        # --- handle input with curses ---
        ch = stdscr.getch()  # returns -1 if no key pressed

        if ch != -1:  # something pressed
            if ch == ord('q'):
                close_flag = True
            elif ch == ord('a'):
                g.move('a', frame_buffer)
            elif ch == ord('d'):
                g.move('d', frame_buffer)
        else:
            g.halt()


        #print the buffer frame
        for y in range(len(frame_buffer)) :
            for x in range(len(frame_buffer[y])) :
                sys.stdout.write(f"\x1b[{y};{x}H" + frame_buffer[y][x])

        
        #push out frame and pause for a frame
        sys.stdout.flush()
        time.sleep(FRAMERATE)
        
        if(close_flag == True) :
            break
   
    #clear terminal when done
    sys.stdout.write("\x1b[2J\x1b[H")


    
    
if __name__=="__main__" :
    curses.wrapper(main)


                






    





