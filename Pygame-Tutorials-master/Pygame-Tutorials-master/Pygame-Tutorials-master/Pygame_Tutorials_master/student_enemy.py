import pygame
pygame.init()

win = pygame.display.set_mode((500,480))

pygame.display.set_caption("First Game")

# Load images for walking and standing
walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
bg = pygame.image.load('bg.jpg')
char = pygame.image.load('standing.png')

clock = pygame.time.Clock()

class player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.left = False
        self.right = False
        self.walkCount = 0
        self.jumpCount = 10
        self.standing = True

    def draw(self, win):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0

        if not(self.standing):
            if self.left:
                win.blit(walkLeft[self.walkCount//3], (self.x,self.y))
                self.walkCount += 1
            elif self.right:
                win.blit(walkRight[self.walkCount//3], (self.x,self.y))
                self.walkCount += 1
        else:
            if self.right:
                win.blit(walkRight[0], (self.x, self.y))
            else:
                win.blit(walkLeft[0], (self.x, self.y))


# Now, students will need to implement the following instructions

# INSTRUCTION 1: Creating the Bullet Class
# Create a new class called `projectile` that represents the bullet.
# This class should include:
# - `x`: the current horizontal position of the bullet
# - `y`: the current vertical position of the bullet
# - `radius`: the radius of the bullet (set this to 6)
# - `color`: the color of the bullet (set this to black, (0, 0, 0))
# - `facing`: direction of the bullet, set it to `1` for right, and `-1` for left

    def draw(self,win):
        pygame.draw.circle(win, self.color, (self.x,self.y), self.radius)


# INSTRUCTION 3: Setting up the Enemy Class
# Create a new class called `enemy` that will represent the enemy in the game.
# This class should include the following attributes:
# - `x`, `y`, `width`, `height`: These will define the enemy’s position and size.
# - `path`: A list of two values, `x` (start position) and `end` (end position).
# - `vel`: Speed of the enemy’s movement (set this to 3).
# - `walkCount`: Counter to handle enemy animation (similar to player’s walkCount).

class enemy(object):

    def draw(self, win):
        self.move()
        if self.walkCount + 1 >= 33:
            self.walkCount = 0
        
        if self.vel > 0:
            win.blit(self.walkRight[self.walkCount//3], (self.x,self.y))
            self.walkCount += 1
        else:
            win.blit(self.walkLeft[self.walkCount//3], (self.x,self.y))
            self.walkCount += 1



# INSTRUCTION 4: Making the Enemy Move
# In the `enemy` class, implement a method `move()` that:
# - Moves the enemy towards the `end` position.
# - Once the enemy reaches the `end`, it should reverse direction.
# - The enemy should keep moving back and forth.


def redrawGameWindow():
    win.blit(bg, (0, 0))
    man.draw(win)
    # INSTRUCTION 6: Add code here to draw the enemy
    # 1. Call `goblin.draw()` here to display the enemy.
    for bullet in bullets:
        bullet.draw(win)
    pygame.display.update()



#mainloop
man = player(200, 410, 64, 64)

# INSTRUCTION 7: Create the enemy instance here
# 1. Create an enemy object: 
#    Example: `goblin = enemy(100, 410, 64, 64, 400)`
goblin = enemy(100, 410, 64, 64, 400)

bullets = []

run = True
while run:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # INSTRUCTION 8: Handle bullet movement
    # 1. Iterate through the `bullets` list.
    # 2. Move the bullet in the `facing` direction.
    # 3. Remove bullets from the list if they go off-screen (i.e., if `x` is less than 0 or greater than 500).

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and man.x > man.vel:
        man.x -= man.vel
        man.left = True
        man.right = False
        man.standing = False
    elif keys[pygame.K_RIGHT] and man.x < 500 - man.width - man.vel:
        man.x += man.vel
        man.right = True
        man.left = False
        man.standing = False
    else:
        man.standing = True
        man.walkCount = 0

    # INSTRUCTION 10: Handle jumping
    if not(man.isJump):
        if keys[pygame.K_UP]:
            man.isJump = True
            man.right = False
            man.left = False
            man.walkCount = 0
    else:
        if man.jumpCount >= -10:
            neg = 1
            if man.jumpCount < 0:
                neg = -1
            man.y -= (man.jumpCount ** 2) * 0.5 * neg
            man.jumpCount -= 1
        else:
            man.isJump = False
            man.jumpCount = 10

    redrawGameWindow()

pygame.quit()
