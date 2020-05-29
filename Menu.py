import pygame


class Menu:

    def __init__(self):
        pygame.init()
        self.width = 1240
        self.height = 480
        pygame.display.set_mode([self.width, self.height])
        self.disp_surface = pygame.display.set_mode((self.width, self.height))

        pygame.display.set_caption('Kasiasty Bartosz')
        self.title_font = pygame.font.SysFont('Veranda', 142)
        self.buttons_font = pygame.font.SysFont('Veranda', 50)

        self.black = pygame.Color('black')
        self.white = pygame.Color('white')

    def display_menu(self):
        run = True
        if run:

            while run:

                self.disp_surface.fill(self.black)

                for event in pygame.event.get():

                    if event.type == pygame.QUIT:
                        run = False

                    if self.was_start_clicked(event):
                        return True

                    elif self.was_quit_clicked(event):
                        pygame.quit()
                        quit()

                self.title = self.title_font.render('Kasiasty Bartosz', True, self.white)
                self.disp_surface.blit(self.title, (220, 50, 800, 200))

                self.start = self.buttons_font.render('Start', True, self.white)
                self.disp_surface.blit(self.start, (225, 320))

                self.stop = self.buttons_font.render('Exit', True, self.white)
                self.disp_surface.blit(self.stop, (945, 320))

                pygame.display.update()

    def was_start_clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if (pygame.mouse.get_pos()[0] >= 225 and pygame.mouse.get_pos()[0] <= 425) and (pygame.mouse.get_pos()[1] >= 320 and pygame.mouse.get_pos()[1] <= 370):
                return True
            else:
                return False

    def was_quit_clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if (pygame.mouse.get_pos()[0] >= 945 and pygame.mouse.get_pos()[0] <= 1482) and (pygame.mouse.get_pos()[1] >= 320 and pygame.mouse.get_pos()[1] <= 370):
                return True
            else:
                return False
