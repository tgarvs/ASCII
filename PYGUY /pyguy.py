


# Example file showing a circle moving on screen
import pygame
import random


class Drop :
    def __init__(self) :

        self.pos = pygame.Vector2(random.randrange(0, width, 1), random.randrange(0, height, 1))
        self.y_speed = random.randrange(6, 9, 1)
        self.x_speed = 2


    def move(self) :
        prev = pygame.Vector2(self.pos.x - self.x_speed, self.pos.y - self.y_speed)
 
        pygame.draw.circle(screen, "green", self.pos, 1)
        pygame.draw.circle(screen, "green", prev, 1)

        if(self.pos.y < height - self.y_speed) :
            self.pos.y = self.pos.y + self.y_speed
        else :
            self.pos.y = 0
        
        if(self.pos.x < width - self.x_speed) :
            self.pos.x = self.pos.x + self.x_speed
        else :
            self.pos.x = 0



class Guy :
    def __init__(self) :
        self.x = screen.x//2
        self.y = screen.y-1
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








if __name__=="__main__" :
    # pygame setup
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    width, height = screen.get_size()
    clock = pygame.time.Clock()
    running = True
    dt = 0

    player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
    rain = [Drop() for _ in range(80)]


    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # fill the screen with a color to wipe away anything from last frame
        screen.fill("black")
        [drop.move() for drop in rain]

        pygame.draw.circle(screen, "red", player_pos, 40)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            player_pos.y -= 300 * dt
        if keys[pygame.K_s]:
            player_pos.y += 300 * dt
        if keys[pygame.K_a]:
            player_pos.x -= 300 * dt
        if keys[pygame.K_d]:
            player_pos.x += 300 * dt

        # flip() the display to put your work on screen
        pygame.display.flip()

        # limits FPS to 60
        # dt is delta time in seconds since last frame, used for framerate-
        # independent physics.
        dt = clock.tick(60) / 1000

    pygame.quit()
                    






        





