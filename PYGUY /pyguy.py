

# Example file showing a circle moving on screen
import pygame
import random
import copy


class Drop :
    def __init__(self) :

        self.pos = pygame.Vector2(random.randrange(0, width, 1), random.randrange(0, height, 1))
        self.prev = copy.deepcopy(self.pos)
        self.y_speed = random.randrange(6, 9, 1)
        self.x_speed = 2
        self.size = 1

    def display(self) : 
        pygame.draw.circle(screen, "green", self.pos, self.size)
        pygame.draw.circle(screen, "green", self.prev, self.size)



    def move(self) :
        if(self.pos.y < height - self.y_speed) :
            self.pos.y = self.pos.y + self.y_speed
        else :
            self.pos.y = 0
        
        if(self.pos.x < width - self.x_speed) :
            self.pos.x = self.pos.x + self.x_speed
        else :
            self.pos.x = 0

        self.prev = pygame.Vector2(self.pos.x - self.x_speed, self.pos.y - self.y_speed)




class Guy :
    def __init__(self) :

        self.moveAmt = 1
        self.maxSpeed = 3
        self.pos = pygame.Vector2(width//2, height-15)
        self.vel = pygame.Vector2(0, 0)
        self.acc = pygame.Vector2(0, 0)

        self.text_surface = my_font.render('&', True, "green")
    

    def display(self) :        
        self.vel.x += self.acc.x
        
        if self.vel.x >= self.maxSpeed :
            self.vel.x = self.maxSpeed
        elif self.vel.x <= -self.maxSpeed :
            self.vel.x = -self.maxSpeed
        
        self.pos.x += self.vel.x

        if self.pos.x > width - abs(self.vel.x) :
            self.pos.x = 1 + abs(self.vel.x)
        elif self.pos.x < abs(self.vel.x) :
            self.pos.x = width - abs(self.vel.x)

        text_rect = self.text_surface.get_rect()
        text_rect.center = self.pos
        screen.blit(self.text_surface, text_rect)


    def move(self, keys) :
        if keys[pygame.K_w]:
            pass
        if keys[pygame.K_s]:
            pass

        if keys[pygame.K_a]:
            self.acc.x -= 1
        if keys[pygame.K_d]:
            self.acc.x += 1

 










if __name__=="__main__" :
    # pygame setup
    pygame.init()
    pygame.font.init()

    screen = pygame.display.set_mode((1280, 720))
    width, height = screen.get_size()
    clock = pygame.time.Clock()
    running = True
    dt = 0

    my_font = pygame.font.SysFont('Arial', 30)

    
    rain = [Drop() for _ in range(80)]
    guy = Guy()


    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # fill the screen with a color to wipe away anything from last frame
        screen.fill("black")
        for drop in rain :
            drop.display()
            drop.move()
        
        guy.display()
        print(guy.pos.x)

        keys = pygame.key.get_pressed()
        guy.move(keys)


        # flip() the display to put your work on screen
        pygame.display.flip()

        # limits FPS to 60
        # dt is delta time in seconds since last frame, used for framerate-
        # independent physics.
        dt = clock.tick(60) / 1000

    pygame.quit()
                    






        





