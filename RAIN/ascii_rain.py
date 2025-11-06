
import time
import sys
import random
import threading
import shutil
import os

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


        
        
# def user_input(cf) :
#     us_in = input()
#     if(us_in == 'm') :
#         speed += 0.001
#     elif(us_in == 'n') :
#         speed -= 0.001

#     if(us_in == 'q') :
#         cf = True

    


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

    # input_thread = threading.Thread(target=user_input, args=(close_flag,))
    # input_thread.start()

    while True:


        sys.stdout.write("\x1b[2J")
        for i in (instances) :
            i.move()
        sys.stdout.flush()
        if(close_flag == True) :
            break
    
    # input_thread.join() #doesn't need to join, but memory safe
    



                






    





