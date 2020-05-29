import pygame
from Characters import *
from Menu import *
import threading

pygame.init()

Characters = Characters()
Menu = Menu()

width = 1240
height = 480
window = pygame.display.set_mode([width, height])
display_surface = pygame.display.set_mode((width, height))

pygame.display.set_caption('Kasiasty Bartosz')

font_for_Characters_friends = pygame.font.SysFont('Veranda', 40)
small_font = pygame.font.SysFont('Veranda', 30)
price_font = pygame.font.SysFont('Veranda', 20)



clock = pygame.time.Clock()

run = Menu.display_menu()

pygame.Surface.fill(display_surface, pygame.Color('black'))

if run:

    thread_guard = threading.Timer((1.0)/60, Characters.increase_money_by_all_characters )
    thread_guard.start()

    while run:
        
        clock.tick(60)

        for event in pygame.event.get():
            

            if event.type == pygame.QUIT:
                run = False

            Characters.check_who_was_bought(event)
            


        if thread_guard.is_alive():
             pass
        else:
            counter_thread = threading.Timer((1.0)/60, Characters.increase_money_by_all_characters )
            thread_guard = counter_thread
            thread_guard.run()
            

        display_surface.blit(Characters.get_image("barto"), (30, 30))

        amount_of_leon = font_for_Characters_friends.render(str(Characters.amount_of_leon) + 'x', True, (255, 255, 255))
        pygame.draw.rect(display_surface, pygame.Color('black'), (280, 30, 100, 100), 0)
        display_surface.blit(amount_of_leon, (330, 80))
        display_surface.blit(Characters.get_image("leon"), (420, 30))
        leon_price = small_font.render('Price: ' + str(Characters.price_of_leon), True, (255, 255, 255))
        pygame.draw.rect(display_surface, pygame.Color('black'), (525, 92, 190, 33), 0)
        display_surface.blit(leon_price, (525, 92))

        amount_of_paczek = font_for_Characters_friends.render( str(Characters.amount_of_paczek) + 'x', True, (255, 255, 255))
        pygame.draw.rect( display_surface, pygame.Color('black'), (770, 30, 100, 100), 0)
        display_surface.blit(amount_of_paczek, (820, 80))
        display_surface.blit(Characters.get_image("paczek"), (910, 30))
        paczek_price = small_font.render('Price: ' + str( Characters.price_of_paczek), True, (255, 255, 255))
        pygame.draw.rect(display_surface, pygame.Color('black'), (1011, 77, 190, 33), 0)
        display_surface.blit(leon_price, (1011, 77))

        amount_of_riko = font_for_Characters_friends.render(str(Characters.amount_of_riko) + 'x', True, (255, 255, 255))
        pygame.draw.rect(display_surface, pygame.Color('black'), (280, 153, 100, 100), 0)
        display_surface.blit(amount_of_riko, (330, 203))
        display_surface.blit(Characters.get_image("riko"), (420, 153))
        riko_price = small_font.render('Price: ' + str(Characters.price_of_riko), True, (255, 255, 255))
        pygame.draw.rect(display_surface, pygame.Color('black'), (525, 198, 192, 50))
        display_surface.blit(riko_price, (525, 198))

        amount_of_katrin = font_for_Characters_friends.render(str( Characters.amount_of_katrin) + 'x', True, (255, 255, 255))
        pygame.draw.rect(display_surface, pygame.Color('black'), (770, 153, 100, 100), 0)
        display_surface.blit(amount_of_katrin, (820, 203))
        display_surface.blit(Characters.get_image("katrin"), (910, 153))
        katrin_price = small_font.render('Price: ' + str( Characters.price_of_katrin), True, (255, 255, 255))
        pygame.draw.rect(display_surface, pygame.Color('black'), (1011, 208, 192, 40))
        display_surface.blit(katrin_price, (1011, 208))

        amount_of_spider = font_for_Characters_friends.render(str(Characters.amount_of_spider) + 'x', True, (255, 255, 255))
        pygame.draw.rect(display_surface, pygame.Color('black'), (280, 276, 100, 100), 0)
        display_surface.blit(amount_of_spider, (330, 326))
        display_surface.blit(Characters.get_image("spider"), (420, 276))
        spider_price = small_font.render('Price: ' + str(Characters.price_of_spider), True, (255, 255, 255))
        pygame.draw.rect(display_surface, pygame.Color('black'), (525, 321, 192, 50))
        display_surface.blit(spider_price, (525, 321))

        amount_of_adalbert = font_for_Characters_friends.render( str( Characters.amount_of_adalbert) + 'x', True, (255, 255, 255))
        pygame.draw.rect(display_surface, pygame.Color('black'), (770, 276, 100, 100), 0)
        display_surface.blit(amount_of_adalbert, (820, 326))
        display_surface.blit(Characters.get_image("adalbert"), (910, 276))
        adalbert_price = small_font.render( 'Price: ' + str( Characters.price_of_adalbert ), True, (255, 255, 255) )
        pygame.draw.rect( display_surface, pygame.Color( 'black' ), (1011, 331, 192, 40) )
        display_surface.blit( adalbert_price, (1011, 331))

        score = small_font.render( '$$$: ' + str(round(Characters.counter, 1)), True, (255, 255, 255))
        pygame.draw.rect(display_surface, pygame.Color('black'), (100, 440, 1240, 30), 0)
        display_surface.blit(score, (100, 440))

        pygame.display.update()

pygame.quit()


