from pygame import *
from Bart import *
import threading
from Menu import *

pygame.init()

def increase_value_by_characters():
    if Bart.amount_of_leon > 0:
        Bart.increase_counter(0.5*Bart.amount_of_leon*(1.0/30))
    if Bart.amount_of_riko > 0:
        Bart.increase_counter(1*Bart.amount_of_riko*(1/30))
    if Bart.amount_of_spider > 0:
        Bart.increase_counter(3*Bart.amount_of_spider*(1/30))
    if Bart.amount_of_paczek > 0:
        Bart.increase_counter(4*Bart.amount_of_paczek*(1/30))
    if Bart.amount_of_katrin > 0:
        Bart.increase_counter(5 * Bart.amount_of_katrin*(1/30))
    if Bart.amount_of_adalbert > 0:
        Bart.increase_counter(10*Bart.amount_of_adalbert*(1/30))

width = 1240
height = 480
window = pygame.display.set_mode([width, height])
display_surface = pygame.display.set_mode((width, height))
pygame.display.set_caption('Kasiasty Bartosz')

font_for_bart_friends = pygame.font.SysFont('Veranda', 40)
small_font = pygame.font.SysFont('Veranda', 30)
price_font = pygame.font.SysFont('Veranda', 20)

Bart = Bart()
Menu = Menu()

clock = pygame.time.Clock()


image_of_bart = pygame.image.load('Barto.png')
image_leon_box = pygame.image.load('Leon_box.png')
image_riko_box = pygame.image.load('Riko_box.png')
image_spider_box = pygame.image.load('Spider_box.png')
image_paczek_box = pygame.image.load('Kapitan_paczek_box.png')
image_katrin_box = pygame.image.load('Katrin_box.png')
image_adalbert_box = pygame.image.load('Adalbert_box.png')

run = Menu.display_menu()
pygame.Surface.fill(display_surface, pygame.Color('black'))

if run:

    while run:
        t2 = threading.Timer((1.0)/30, increase_value_by_characters )
        for event in pygame.event.get():
            clock.tick(60)

            if event.type == pygame.QUIT:
                run = False

            if Bart.was_bart_clicked(event) == True:
                Bart.increase_counter()

            if Bart.was_leon_clicked(event) == True:
                Bart.possibility_to_buy_leon()

            if Bart.was_riko_clicked(event) == True:
                Bart.possibility_to_buy_riko()

            if Bart.was_spider_clicked(event) == True:
                Bart.possibility_to_buy_spider()

            if Bart.was_paczek_clicked(event) == True:
                Bart.possibility_to_buy_paczek()

            if Bart.was_katrin_clicked(event) == True:
                Bart.possibility_to_buy_katrin()

            if Bart.was_adalbert_clicked(event) == True:
                Bart.possibility_to_buy_adalbert()


        clock.tick(60)

        if t2.is_alive():
            pass
        else:
            t2.run()

        display_surface.blit(image_of_bart, (30, 30))

        amount_of_leon = font_for_bart_friends.render(str(Bart.amount_of_leon) + 'x', True, (255, 255, 255))
        pygame.draw.rect(display_surface, pygame.Color('black'), (280, 30, 100, 100), 0)
        display_surface.blit(amount_of_leon, (330, 80))
        display_surface.blit(image_leon_box, (420, 30))
        leon_price = small_font.render('Price: ' + str(Bart.price_of_leon), True, (255, 255, 255))
        pygame.draw.rect(display_surface, pygame.Color('black'), (525, 92, 190, 33), 0)
        display_surface.blit(leon_price, (525, 92))

        amount_of_paczek = font_for_bart_friends.render( str(Bart.amount_of_paczek) + 'x', True, (255, 255, 255))
        pygame.draw.rect( display_surface, pygame.Color('black'), (770, 30, 100, 100), 0)
        display_surface.blit(amount_of_paczek, (820, 80))
        display_surface.blit(image_paczek_box, (910, 30))
        leon_price = small_font.render('Price: ' + str( Bart.price_of_paczek), True, (255, 255, 255))
        pygame.draw.rect(display_surface, pygame.Color('black'), (1011, 77, 190, 33), 0)
        display_surface.blit(leon_price, (1011, 77))

        amount_of_riko = font_for_bart_friends.render(str(Bart.amount_of_riko) + 'x', True, (255, 255, 255))
        pygame.draw.rect(display_surface, pygame.Color('black'), (280, 153, 100, 100), 0)
        display_surface.blit(amount_of_riko, (330, 203))
        display_surface.blit(image_riko_box, (420, 153))
        riko_price = small_font.render('Price: ' + str(Bart.price_of_riko), True, (255, 255, 255))
        pygame.draw.rect(display_surface, pygame.Color('black'), (525, 198, 192, 50))
        display_surface.blit(riko_price, (525, 198))

        amount_of_katrin = font_for_bart_friends.render(str( Bart.amount_of_katrin) + 'x', True, (255, 255, 255))
        pygame.draw.rect(display_surface, pygame.Color('black'), (770, 153, 100, 100), 0)
        display_surface.blit(amount_of_katrin, (820, 203))
        display_surface.blit(image_katrin_box, (910, 153))
        katrin_price = small_font.render('Price: ' + str( Bart.price_of_katrin), True, (255, 255, 255))
        pygame.draw.rect(display_surface, pygame.Color('black'), (1011, 208, 192, 40))
        display_surface.blit(katrin_price, (1011, 208))

        amount_of_spider = font_for_bart_friends.render(str(Bart.amount_of_spider) + 'x', True, (255, 255, 255))
        pygame.draw.rect(display_surface, pygame.Color('black'), (280, 276, 100, 100), 0)
        display_surface.blit(amount_of_spider, (330, 326))
        display_surface.blit(image_spider_box, (420, 276))
        spider_price = small_font.render('Price: ' + str(Bart.price_of_spider), True, (255, 255, 255))
        pygame.draw.rect(display_surface, pygame.Color('black'), (525, 321, 192, 50))
        display_surface.blit(spider_price, (525, 321))

        amount_of_adalbert = font_for_bart_friends.render( str( Bart.amount_of_adalbert) + 'x', True, (255, 255, 255))
        pygame.draw.rect(display_surface, pygame.Color('black'), (770, 276, 100, 100), 0)
        display_surface.blit(amount_of_adalbert, (820, 326))
        display_surface.blit(image_adalbert_box, (910, 276))
        adalbert_price = small_font.render( 'Price: ' + str( Bart.price_of_adalbert ), True, (255, 255, 255) )
        pygame.draw.rect( display_surface, pygame.Color( 'black' ), (1011, 331, 192, 40) )
        display_surface.blit( adalbert_price, (1011, 331))

        score = small_font.render( '$$$: ' + str(round(Bart.counter, 2)), True, (255, 255, 255))
        pygame.draw.rect(display_surface, pygame.Color('black'), (100, 440, 1240, 30), 0)
        display_surface.blit(score, (100, 440))

        pygame.display.update()

pygame.quit()


