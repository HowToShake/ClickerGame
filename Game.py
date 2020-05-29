import pygame
from Characters import *
import threading


class Game:

    def __init__(self):
        pygame.init()
        self.width = 1240
        self.height = 480
        self.window = pygame.display.set_mode([self.width, self.height])
        self.disp_surface = pygame.display.set_mode((self.width, self.height))

        pygame.display.set_caption('Kasiasty Bartosz')

        self.characters_font = pygame.font.SysFont('Veranda', 40)
        self.small_font = pygame.font.SysFont('Veranda', 30)

        self.Characters = Characters()

        self.black = pygame.Color('black')
        self.white = pygame.Color('white')
        self.clock = pygame.time.Clock()

    def display(self, character):
        amount = str(self.Characters.get_char_info("amount", character))+'x'
        price = 'Price:'+str(self.Characters.get_char_info("price", character))
        display_amount = self.characters_font.render(amount, True, self.white)
        display_price = self.small_font.render(price, True, self.white)
        image = self.Characters.get_image(character)

        if character is "leon":
            self.disp_surface.blit(display_amount, (330, 80))
            self.disp_surface.blit(image, (420, 30))
            self.disp_surface.blit(display_price, (525, 92))
        elif character is "paczek":
            self.disp_surface.blit(display_amount, (820, 80))
            self.disp_surface.blit(image, (910, 30))
            self.disp_surface.blit(display_price, (1011, 77))
        elif character is "riko":
            self.disp_surface.blit(display_amount, (330, 203))
            self.disp_surface.blit(image, (420, 153))
            self.disp_surface.blit(display_price, (525, 198))
        elif character is "katrin":
            self.disp_surface.blit(display_amount, (820, 203))
            self.disp_surface.blit(image, (910, 153))
            self.disp_surface.blit(display_price, (1011, 208))
        elif character is "spider":
            self.disp_surface.blit(display_amount, (330, 326))
            self.disp_surface.blit(image, (420, 276))
            self.disp_surface.blit(display_price, (525, 321))
        elif character is "adalbert":
            self.disp_surface.blit(display_amount, (820, 326))
            self.disp_surface.blit(image, (910, 276))
            self.disp_surface.blit(display_price, (1011, 331))
        elif character is "barto":
            self.disp_surface.blit(image, (30, 30))

    def display_score(self):
        score = '$$$: ' + str(round(self.Characters.counter, 1))
        disp_score = self.small_font.render(score, True, self.white)
        self.disp_surface.blit(disp_score, (100, 440))

    def display_game(self, run):
        pygame.Surface.fill(self.disp_surface, self.black)
        T = (1.0)/60
        score_ctr = self.Characters.increase_money_by_all_characters

        if run:

            thread_guard = threading.Timer(T, score_ctr)
            thread_guard.start()

            while run:

                self.clock.tick(60)
                self.disp_surface.fill(self.black)

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        run = False

                    self.Characters.check_who_was_bought(event)

                if not thread_guard.is_alive():
                    ctr_thread = threading.Timer((1.0)/60, score_ctr)
                    thread_guard = ctr_thread
                    thread_guard.run()

                self.display("barto")
                self.display("leon")
                self.display("paczek")
                self.display("riko")
                self.display("spider")
                self.display("katrin")
                self.display("adalbert")
                self.display_score()

                pygame.display.update()

    pygame.quit()
