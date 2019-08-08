import pygame

class Menu:

    def __init__(self):
        pygame.init()
        self.width = 1240
        self.height = 480
        self.window = pygame.display.set_mode( [self.width, self.height] )
        self.display_surface = pygame.display.set_mode( (self.width, self.height) )
        pygame.display.set_caption( 'Kasiasty Bartosz' )
        self.title_font = pygame.font.SysFont( 'Veranda', 142 )
        self.buttons_font = pygame.font.SysFont('Veranda', 50)




    def display_menu(self):
        run = True
        if run:

            while run:

                for event in pygame.event.get():

                    if event.type == pygame.QUIT:
                        run = False

                    if self.was_start_clicked(event) == True:
                        return True

                    if self.was_quit_clicked(event) == True:
                        pygame.quit()
                        quit()
                        return False



                self.title = self.title_font.render('Kasiasty Bartosz', True, (255,255,255))
                pygame.draw.rect(self.display_surface, pygame.Color( 'black' ), (220, 50, 800, 200), 0 )
                self.display_surface.blit(self.title, (220, 50, 800, 200))


                self.start = self.buttons_font.render('Start',True, (255, 255, 255))
                pygame.draw.rect( self.display_surface, pygame.Color( 'black' ), (225, 320, 200, 50), 0 )
                self.display_surface.blit(self.start, (225,320))


                self.stop = self.buttons_font.render('Stop', True, (255, 255, 255))
                pygame.draw.rect( self.display_surface, pygame.Color( 'black' ), (945, 320, 200, 50), 0 )
                self.display_surface.blit(self.stop, (945, 320))
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





