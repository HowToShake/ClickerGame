import pygame

class Characters:

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
        self.image_of_self = pygame.image.load('./pics/Barto.png')
        self.image_leon_box = pygame.image.load('./pics/Leon_box.png')
        self.image_riko_box = pygame.image.load('./pics/Riko_box.png')
        self.image_spider_box = pygame.image.load('./pics/Spider_box.png')
        self.image_paczek_box = pygame.image.load('./pics/Kapitan_paczek_box.png')
        self.image_katrin_box = pygame.image.load('./pics/Katrin_box.png')
        self.image_adalbert_box = pygame.image.load('./pics/Adalbert_box.png')




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


    def buy_leon(self):
        if  self.counter >= self.price_of_leon:

            self.amount_of_leon += 1
            self.counter = self.counter - self.price_of_leon
            self.price_of_leon += 5

    def was_riko_clicked(self,event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if (pygame.mouse.get_pos()[0] >= 420 and pygame.mouse.get_pos()[0] <= 720) and (pygame.mouse.get_pos()[1] >= 153 and pygame.mouse.get_pos()[1] <= 253):
                    return True
            else:
                    return False


    def buy_riko(self):
        if  self.counter >= self.price_of_riko:
            self.amount_of_riko += 1
            self.counter = self.counter - self.price_of_riko
            self.price_of_riko += 50



    def was_spider_clicked(self,event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if (pygame.mouse.get_pos()[0] >= 420 and pygame.mouse.get_pos()[0] <= 720) and (pygame.mouse.get_pos()[1] >= 276 and pygame.mouse.get_pos()[1] <= 376):
                    return True
            else:
                    return False


    def buy_spider(self):
        if  self.counter >= self.price_of_spider:
            self.amount_of_spider += 1
            self.counter = self.counter - self.price_of_spider
            self.price_of_spider += 1000

    def was_paczek_clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if (pygame.mouse.get_pos()[0] >= 910 and pygame.mouse.get_pos()[0] <= 1210) and (pygame.mouse.get_pos()[1] >= 30 and pygame.mouse.get_pos()[1] <= 130):
                return True
            else:
                return False


    def buy_paczek(self):
        if self.counter >= self.price_of_paczek:
            self.amount_of_paczek += 1
            self.counter = self.counter - self.price_of_paczek
            self.price_of_paczek += 3500



    def was_katrin_clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if (pygame.mouse.get_pos()[0] >= 910 and pygame.mouse.get_pos()[0] <= 1210) and (pygame.mouse.get_pos()[1] >= 153 and pygame.mouse.get_pos()[1] <= 253):
                return True
            else:
                return False


    def buy_katrin(self):
        if self.counter >= self.price_of_katrin:
            self.amount_of_katrin += 1
            self.counter = self.counter - self.price_of_katrin
            self.price_of_katrin += 10000



    def was_adalbert_clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if (pygame.mouse.get_pos()[0] >= 910 and pygame.mouse.get_pos()[0] <= 1210) and (pygame.mouse.get_pos()[1] >= 276 and pygame.mouse.get_pos()[1] <= 376):
                return True
            else:
                return False


    def buy_adalbert(self):
        if self.counter >= self.price_of_adalbert:
            self.amount_of_adalbert += 1
            self.counter = self.counter - self.price_of_adalbert
            self.price_of_adalbert += 50000


    def check_who_was_bought(self, event):
        if self.was_bart_clicked(event):
            self.increase_counter()

        elif self.was_leon_clicked(event):
            self.buy_leon()

        elif self.was_riko_clicked(event):
            self.buy_riko()

        elif self.was_spider_clicked(event):
            self.buy_spider()

        elif self.was_paczek_clicked(event):
            self.buy_paczek()

        elif self.was_katrin_clicked(event):
            self.buy_katrin()

        elif self.was_adalbert_clicked(event):
            self.buy_adalbert()


    def increase_amount_of_character(self):
        if self.amount_of_leon > 0:
            self.increase_counter(0.5*self.amount_of_leon)
        
        if self.amount_of_riko > 0:
            self.increase_counter(self.amount_of_riko)
        
        if self.amount_of_spider > 0:
            self.increase_counter(3*self.amount_of_spider)
        
        if self.amount_of_paczek > 0:
            self.increase_counter(4*self.amount_of_paczek)
        
        if self.amount_of_katrin > 0:
            self.increase_counter(5 * self.amount_of_katrin)
        
        if self.amount_of_adalbert > 0:
            self.increase_counter(10*self.amount_of_adalbert)


    def increase_money_by_all_characters(self):
        amount = 0.5*self.amount_of_leon + self.amount_of_riko + 3*self.amount_of_spider + 4*self.amount_of_paczek + 5 * self.amount_of_katrin + 10*self.amount_of_adalbert
        self.increase_counter((1/60)*amount)

    def is_none_character_bought(self):
        if(self.amount_of_adalbert == 0 and self.amount_of_katrin == 0 and self.amount_of_leon == 0 and self.amount_of_paczek == 0 and self.amount_of_riko == 0 and self.amount_of_spider == 0):
            return True
        return False

    def get_image(self,character):
        images = [self.image_of_self, self.image_leon_box , self.image_riko_box, self.image_spider_box, self.image_paczek_box ,self.image_katrin_box, self.image_adalbert_box]
        if character is "all":
            return  images
        elif character is "barto":
            return images[0]
        elif character is "leon":
            return images[1]
        elif character is "riko":
            return images[2]
        elif character is "spider":
            return images[3]
        elif character is "paczek":      
            return images[4]
        elif character is "katrin":
            return images[5]
        elif character is "adalbert":
            return images[6]











