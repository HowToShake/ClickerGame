from pygame import *
from Game import *
from Menu import *

pygame.init()

Game = Game()
Menu = Menu()

was_game_choosen = Menu.display_menu()

if(was_game_choosen):
    Game.display_game(was_game_choosen)

pygame.quit()
