import pygame

class Bart:

    def __init__(self,counter: int=0,):
        self.counter = counter
        self.amount_of_leon = 0
        self.price_of_leon = 25
        self.amount_of_riko = 0
        self.price_of_riko = 150
        self.amount_of_spider = 0
        self.price_of_spider = 1000
        self.amount_of_paczek = 0
        self.price_of_paczek = 7000
        self.amount_of_katrin = 0
        self.price_of_katrin = 15000
        self.amount_of_adalbert = 0
        self.price_of_adalbert = 50000


    def increase_counter(self,value: float=1):
        self.counter += value
        return self.counter


    def was_bart_clicked(self,event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if (pygame.mouse.get_pos()[0]>30 and pygame.mouse.get_pos()[0]<230) and (pygame.mouse.get_pos()[1]>30 and pygame.mouse.get_pos()[1]<400):
                return True
            else:
                return False


    def was_leon_clicked(self,event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if (pygame.mouse.get_pos()[0] >= 420 and pygame.mouse.get_pos()[0] <= 720) and (pygame.mouse.get_pos()[1] >= 30 and pygame.mouse.get_pos()[1] <= 130):
                    return True
            else:
                    return False


    def possibility_to_buy_leon(self):
        if self.counter >= self.price_of_leon:
            self.amount_of_leon += 1
            self.counter = self.counter - self.price_of_leon
            self.price_of_leon += 5
        else:
            print('You dont have money!')


    def was_riko_clicked(self,event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if (pygame.mouse.get_pos()[0] >= 420 and pygame.mouse.get_pos()[0] <= 720) and (pygame.mouse.get_pos()[1] >= 153 and pygame.mouse.get_pos()[1] <= 253):
                    return True
            else:
                    return False


    def possibility_to_buy_riko(self):
        if  self.counter >= self.price_of_riko:
            self.amount_of_riko += 1
            self.counter = self.counter - self.price_of_riko
            self.price_of_riko += 50
        else:
            print('You dont have money!')


    def was_spider_clicked(self,event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if (pygame.mouse.get_pos()[0] >= 420 and pygame.mouse.get_pos()[0] <= 720) and (pygame.mouse.get_pos()[1] >= 276 and pygame.mouse.get_pos()[1] <= 376):
                    return True
            else:
                    return False


    def possibility_to_buy_spider(self):
        if  self.counter >= self.price_of_spider:
            self.amount_of_spider += 1
            self.counter = self.counter - self.price_of_spider
            self.price_of_spider += 1000
        else:
            print('You dont have money!')

    def was_paczek_clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if (pygame.mouse.get_pos()[0] >= 910 and pygame.mouse.get_pos()[0] <= 1210) and (pygame.mouse.get_pos()[1] >= 30 and pygame.mouse.get_pos()[1] <= 130):
                return True
            else:
                return False


    def possibility_to_buy_paczek(self):
        if self.counter >= self.price_of_paczek:
            self.amount_of_paczek += 1
            self.counter = self.counter - self.price_of_paczek
            self.price_of_paczek += 3500
        else:
            print( 'You dont have money!' )


    def was_katrin_clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if (pygame.mouse.get_pos()[0] >= 910 and pygame.mouse.get_pos()[0] <= 1210) and (pygame.mouse.get_pos()[1] >= 153 and pygame.mouse.get_pos()[1] <= 253):
                return True
            else:
                return False


    def possibility_to_buy_katrin(self):
        if self.counter >= self.price_of_katrin:
            self.amount_of_katrin += 1
            self.counter = self.counter - self.price_of_katrin
            self.price_of_katrin += 10000
        else:
            print( 'You dont have money!' )


    def was_adalbert_clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if (pygame.mouse.get_pos()[0] >= 910 and pygame.mouse.get_pos()[0] <= 1210) and (pygame.mouse.get_pos()[1] >= 276 and pygame.mouse.get_pos()[1] <= 376):
                return True
            else:
                return False


    def possibility_to_buy_adalbert(self):
        if self.counter >= self.price_of_adalbert:
            self.amount_of_adalbert += 1
            self.counter = self.counter - self.price_of_adalbert
            self.price_of_adalbert += 50000
        else:
            print( 'You dont have money!' )














