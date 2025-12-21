

# Example file showing a circle moving on screen
import pygame
import random
import copy
import pygame.freetype


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

        self.moveAmt = 0.5
        self.maxSpeed = 10
        self.pos = pygame.Vector2(width//2, height-10)
        self.vel = pygame.Vector2(0, 0)
        self.acc = pygame.Vector2(0, 0)
        self.prev_keys = pygame.key.get_pressed()

        # self.text_surface = my_font.render('&', False, "green")
        self.text_surface, _ = ft_font.render("&", fgcolor=(0, 255, 0), bgcolor=None)

    
    def input_check(self, keys) :
        #stop if 
        if self.prev_keys != keys :
            self.acc.x = 0
            self.vel.x = 0    

        #check current keys
        if keys[pygame.K_w]:
            pass
        if keys[pygame.K_s]:
            pass

        if keys[pygame.K_a]:
            self.acc.x -= self.moveAmt
        elif keys[pygame.K_d]:
            self.acc.x += self.moveAmt
        else :
            self.acc.x = 0
            self.vel.x = 0

        self.prev_keys = keys


    def display(self) :        
        text_rect = self.text_surface.get_rect()
        text_rect.center = self.pos
        screen.blit(self.text_surface, text_rect)


    def move(self, keys) : #event: pygame.event) :
        self.input_check(keys)

        #actually make it move
        self.vel.x += self.acc.x
        
        #speed check
        if self.vel.x >= self.maxSpeed :
            self.vel.x = self.maxSpeed
        elif self.vel.x <= -self.maxSpeed :
            self.vel.x = -self.maxSpeed
        
        self.pos.x += self.vel.x

        #bounds check
        if self.pos.x > width - abs(self.vel.x) :
            self.pos.x = 1 + abs(self.vel.x)
        elif self.pos.x < abs(self.vel.x) :
            self.pos.x = width - abs(self.vel.x)






def apply_scanlines(screen):
    width, height = screen.get_size()
    scanline_surface = pygame.Surface((width, height), pygame.SRCALPHA)

    for y in range(0, height, 4):
        pygame.draw.line(scanline_surface, (0, 0, 0, 60), (0, y), (width, y))

    screen.blit(scanline_surface, (0, 0))


def apply_flicker(screen):
    if random.randint(0, 20) == 0:
        flicker_surface = pygame.Surface(screen.get_size(), pygame.SRCALPHA)
        flicker_surface.fill((255, 255, 255, 5))
        screen.blit(flicker_surface, (0, 0))


def apply_glow(screen):
    width, height = screen.get_size()
    glow_surf = pygame.transform.smoothscale(screen, (width // 2, height // 2))
    glow_surf = pygame.transform.smoothscale(glow_surf, (width, height))
    glow_surf.set_alpha(50)
    screen.blit(glow_surf, (0, 0))





if __name__=="__main__" :
    # pygame setup
    pygame.init()
    pygame.font.init()
    pygame.freetype.init() 

    screen = pygame.display.set_mode((1280, 720))
    width, height = screen.get_size()
    clock = pygame.time.Clock()
    running = True
    dt = 0

    my_font = pygame.font.SysFont('Arial', 50)
    ft_font = pygame.freetype.SysFont('Arial', 25) 

    
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
        keys = pygame.key.get_pressed()
        guy.move(keys)
        
        # apply_flicker(screen)
        # apply_scanlines(screen)
        # apply_glow(screen)

        # flip() the display to put your work on screen
        pygame.display.flip()

        # limits FPS to 60
        dt = clock.tick(60) / 1000

    pygame.quit()
                    






        





