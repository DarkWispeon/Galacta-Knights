import pygame
pygame.font.init()
pygame.mixer.init()

print("\033c")


#defines the height and width of the window
WIDTH, HEIGHT = 1600, 1000
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

#sets the name of the window
pygame.display.set_caption("Galacta Knights")

#changes the defauslt icon of the window
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)


#definig certain game variables
MAX_BULL = 6
FPS = 60
BULL_VEL = 15
VEL = 10
HP = 20

#sound managment
LASER_HIT = pygame.mixer.Sound('hit.wav')
pygame.mixer.Sound.set_volume(LASER_HIT, 0.5)
LASER_SHOOT = pygame.mixer.Sound('shot.wav')
DEAD_SFX = pygame.mixer.Sound('ded.wav')
BGM = pygame.mixer.Sound('bgm.mp3')
pygame.mixer.Sound.set_volume(BGM, 0.3)

#font for the game
FONT = pygame.font.SysFont('retrogaming', 40)

#hitboxes
BORDER = pygame.Rect(0, HEIGHT//2, WIDTH, 2.5)
WHITE_SHIP = pygame.image.load("wit.png")
PURPLE_SHIP = pygame.image.load("purp.png")
BG = pygame.transform.scale(pygame.image.load("bg.png"),(WIDTH, HEIGHT))

#laser images
LASER_R = pygame.image.load("red_laser.png")
LASER_G = pygame.image.load("green_laser.png")

#collision events
PURP_HIT = pygame.USEREVENT + 1
WIT_HIT = pygame.USEREVENT + 2

#Starts the background music
BGM.play()    
pygame.mixer.pause()


#function for dealing with the laser movement, collision, etc.
def handle_lasers(laser_g, laser_r, wit, purp):
    for bullet1 in laser_r:
        bullet1.y += BULL_VEL
        if purp.colliderect(bullet1):
            pygame.event.post(pygame.event.Event(PURP_HIT))
            laser_r.remove(bullet1)
        elif bullet1.y > HEIGHT:
             laser_r.remove(bullet1)
        


    for bullet1 in laser_g:
        bullet1.y -= BULL_VEL
        if wit.colliderect(bullet1):
            pygame.event.post(pygame.event.Event(WIT_HIT))
            laser_g.remove(bullet1)
        elif bullet1.y < 0:
             laser_g.remove(bullet1)

    for bullet2 in laser_r:
        bullet2.y += BULL_VEL
        if purp.colliderect(bullet2):
            pygame.event.post(pygame.event.Event(PURP_HIT))
            laser_r.remove(bullet2)
        elif bullet2.y > HEIGHT:
             laser_r.remove(bullet2)

    for bullet2 in laser_g:
        bullet2.y -= BULL_VEL
        if wit.colliderect(bullet2):
            pygame.event.post(pygame.event.Event(WIT_HIT))
            laser_g.remove(bullet2)
        elif bullet2.y < 0:
             laser_g.remove(bullet2)


#updates the window
def draw_window(wit, purp, laser_g, laser_r, wit_hp, purp_hp):
    WIN.blit(BG, (0, 0))
    pygame.draw.rect(WIN, (0, 204, 0), BORDER)
    WIN.blit(WHITE_SHIP, (wit.x, wit.y))
    WIN.blit(PURPLE_SHIP, (purp.x, purp.y))

    if wit_hp >= 19:
        wit_hp_image = pygame.image.load('sprite_00.png')

    elif wit_hp >= 17 and wit_hp < 19:
        wit_hp_image = pygame.image.load('sprite_01.png')

    elif wit_hp >= 15 and wit_hp < 17:
        wit_hp_image = pygame.image.load('sprite_02.png')

    elif wit_hp >= 13 and wit_hp < 15:
        wit_hp_image = pygame.image.load('sprite_03.png')

    elif wit_hp >= 11 and wit_hp < 13:
        wit_hp_image = pygame.image.load('sprite_04.png')

    elif wit_hp >= 9 and wit_hp < 11:
        wit_hp_image = pygame.image.load('sprite_05.png')

    elif wit_hp >= 7 and wit_hp < 9:
        wit_hp_image = pygame.image.load('sprite_06.png')

    elif wit_hp >= 5 and wit_hp < 7:
        wit_hp_image = pygame.image.load('sprite_07.png')

    elif wit_hp >= 3 and wit_hp < 5:
        wit_hp_image = pygame.image.load('sprite_08.png')

    elif wit_hp >= 0 and wit_hp < 3:
        wit_hp_image = pygame.image.load('sprite_09.png')
    
    if purp_hp >= 19:
        purp_hp_image = pygame.image.load('sprite_00.png')

    elif purp_hp >= 17 and purp_hp < 19:
        purp_hp_image = pygame.image.load('sprite_01.png')

    elif purp_hp >= 15 and purp_hp < 17:
        purp_hp_image = pygame.image.load('sprite_02.png')

    elif purp_hp >= 13 and purp_hp < 15:
        purp_hp_image = pygame.image.load('sprite_03.png')

    elif purp_hp >= 11 and purp_hp < 13:
        purp_hp_image = pygame.image.load('sprite_04.png')

    elif purp_hp >= 9 and purp_hp < 11:
        purp_hp_image = pygame.image.load('sprite_05.png')

    elif purp_hp >= 7 and purp_hp < 9:
        purp_hp_image = pygame.image.load('sprite_06.png')

    elif purp_hp >= 5 and purp_hp < 7:
        purp_hp_image = pygame.image.load('sprite_07.png')

    elif purp_hp >= 3 and purp_hp < 5:
        purp_hp_image = pygame.image.load('sprite_08.png')

    elif purp_hp >= 0 and purp_hp < 3:
        purp_hp_image = pygame.image.load('sprite_09.png')

  


    

    purp_hp_image = pygame.transform.scale(purp_hp_image, (80,5))
    wit_hp_image = pygame.transform.scale(wit_hp_image, (80,5))
    WIN.blit(wit_hp_image, (wit.x , wit.y - 15))
    WIN.blit(purp_hp_image, (purp.x, purp.y + 90))
    


    for bullet1 in laser_r:
        WIN.blit(LASER_R, (bullet1.x, bullet1.y))

    for bullet2 in laser_r:
         WIN.blit(LASER_R, (bullet2.x, bullet2.y))

    for bullet2 in laser_g:
         WIN.blit(LASER_G, (bullet2.x, bullet2.y))
        
    for bullet1 in laser_g:
         WIN.blit(LASER_G, (bullet1.x, bullet1.y))    

    pygame.display.update()

#movement for the white ship
def handle_movement_wit(keys_pressed, wit):

        if keys_pressed[pygame.K_w] and wit.y - VEL > -5:
            wit.y -= 10

        if keys_pressed[pygame.K_s] and wit.y + VEL + wit.height < BORDER.y:
            wit.y += 10

        if keys_pressed[pygame.K_a] and wit.x - VEL > -5:
            wit.x -= 10

        if keys_pressed[pygame.K_d] and wit.x + VEL + wit.height < WIDTH:
            wit.x += 10

        if keys_pressed[pygame.K_y]:
    
            if keys_pressed[pygame.K_w] and wit.y - VEL > -5:
                wit.y -= 50

            if keys_pressed[pygame.K_s] and wit.y + VEL + wit.height < BORDER.y:
                wit.y += 50

            if keys_pressed[pygame.K_a] and wit.x - VEL > -5:
                wit.x -= 50

            if keys_pressed[pygame.K_d] and wit.x + VEL + wit.height < WIDTH:
                wit.x += 50

#movement for the purple ship
def handle_movement_purp(keys_pressed, purp):
        if keys_pressed[pygame.K_UP]and purp.y - VEL + 10 > BORDER.y:
            purp.y -= 10

        if keys_pressed[pygame.K_DOWN]and purp.y + VEL + purp.height < HEIGHT:
            purp.y += 10

        if keys_pressed[pygame.K_LEFT]and purp.x - VEL >  BORDER.height - 5:
            purp.x -= 10

        if keys_pressed[pygame.K_RIGHT]and purp.x + VEL + purp.height < WIDTH:
            purp.x += 10

        if keys_pressed[pygame.K_o]:
            if keys_pressed[pygame.K_UP]and purp.y - VEL + 10 > BORDER.y:
                purp.y -= 50

            if keys_pressed[pygame.K_DOWN]and purp.y + VEL + purp.height < HEIGHT:
                purp.y += 50

            if keys_pressed[pygame.K_LEFT]and purp.x - VEL >  BORDER.height - 5:
                purp.x -= 50

            if keys_pressed[pygame.K_RIGHT]and purp.x + VEL + purp.height < WIDTH:
                purp.x += 50

#when the winner is determined
def winner(text):
    drw_txt = FONT.render(text, 1, (255,255,255))
    pygame.mixer.pause()
    DEAD_SFX.play()
    trophy = pygame.image.load('trophy.png')
    trophy = pygame.transform.scale(trophy, (600,600))
    banner = pygame.image.load('banner.png')
    banner = pygame.transform.scale(banner, (600,600))
    WIN.blit(trophy, (WIDTH//2 - trophy.get_width()/2, HEIGHT//2 - trophy.get_height()/2 + 40))
    WIN.blit(banner, (WIDTH//2 - banner.get_width()/2, HEIGHT//2 - banner.get_height()/2 + 40))
    WIN.blit(drw_txt,(WIDTH//2 - drw_txt.get_width()/2, HEIGHT//2 - drw_txt.get_height()/2))
    pygame.display.update()
    pygame.time.delay(5000)


#main function for the game
def main():
    pygame.mixer.unpause()
    wit = pygame.Rect(900, 250,75,75)
    purp = pygame.Rect(900, 750,75,75)
    lasers_r = []
    lasers_g = []
    wit_health = HP
    purp_health = HP
    clock = pygame.time.Clock()
    run = True
    while run:
        keys_pressed = pygame.key.get_pressed()
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()


            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p and len(lasers_g) < MAX_BULL:
                        bullet1 = pygame.Rect(purp.x + 10, purp.y + 10,10,5)
                        bullet2 = pygame.Rect(purp.x + 55, purp.y + 10,10,5)
                        lasers_g.append(bullet1)
                        lasers_g.append(bullet2)
                        LASER_SHOOT.play()

                        
                if event.key == pygame.K_t and len(lasers_r) < MAX_BULL:
                        bullet1 = pygame.Rect(wit.x + 10, wit.y,10,5)
                        bullet2 = pygame.Rect(wit.x  + 55, wit.y,5,10)
                        lasers_r.append(bullet1)
                        lasers_r.append(bullet2)
                        LASER_SHOOT.play()

            if event.type == WIT_HIT:
                 wit_health -= 1
                 LASER_HIT.play()

            if event.type == PURP_HIT:
                 purp_health -= 1
                 LASER_HIT.play()



        win_text = ""
        if wit_health <= 0:
             win_text = "Purple Wins!"
             
        if purp_health <= 0:
             win_text = "White Wins!"

        if win_text != "":
             winner(win_text)
             pygame.mixer.pause()
             main()

        handle_lasers(lasers_g,lasers_r,wit,purp)
        handle_movement_purp(keys_pressed, purp)
        handle_movement_wit(keys_pressed, wit)
        draw_window(wit,purp,lasers_g,lasers_r, wit_health, purp_health) 
        
        


#game initialization        
if __name__ == "__main__":
    main()   
    
