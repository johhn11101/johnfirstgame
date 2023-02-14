import pygame

# Initialize pygame
pygame.init()

# Set up the display window
screen = pygame.display.set_mode((360, 600)) 
clock = pygame.time.Clock()

# Load the background image
background = pygame.image.load('background.png').convert()
planet_images = ['p_one.png', 'p_two.png', 'p_three.png']
planet_index = 0
planet = pygame.image.load(planet_images[planet_index])

# Initialize the planet position
planet_x = 140
planet_y = 50
fired = False
bullet_y = 500

# Blit the background and planet onto the screen
screen.blit(background, [0, 0])
screen.blit(planet, [planet_x, planet_y])
screen.blit(pygame.image.load('spaceship.png'), [160, 500])
screen.blit(pygame.image.load('bullet.png'), [180, bullet_y])

# Update the display
pygame.display.update()

# Game loop
running = True
move_direction = 'right'
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Handle the bullet firing
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        fired = True
        
    if fired:
        bullet_y -= 10
        if bullet_y == 50:
            fired = False
            bullet_y = 500
    
    # Check for a collision between the bullet and the planet
    if bullet_y < 80 and 120 < planet_x < 180:
        planet_index += 1
        if planet_index < len(planet_images):
            planet = pygame.image.load(planet_images[planet_index])
            planet_x = 10
        else:
            print("YOU WIN")
            running = False
    
    # Keep the images displayed for longer by adding a delay
    pygame.time.wait(50)

    # Update the planet position
    if move_direction == 'right':
        planet_x += 5
        if planet_x == 300:
            move_direction = 'left'
    else:
        planet_x -= 5
        if planet_x == 0:
            move_direction = 'right'
        
    # Re-blit the background and updated planet position
    screen.blit(background, [0, 0])
    screen.blit(planet, [planet_x, planet_y])
    screen.blit(pygame.image.load('spaceship.png'), [160, 500])
    screen.blit(pygame.image.load('bullet.png'), [180, bullet_y])

    # Update the display
    pygame.display.update()
    clock.tick(60)

# Quit pygame
pygame.quit()
