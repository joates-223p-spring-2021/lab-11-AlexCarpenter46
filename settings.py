#this is the settings file 
#set whatever you like here

class Settings : 

    def __init__(self):

        #The screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        #Ship settings now
        self.ship_speed = 1.5

        #Bullet settings
        self.bullet_speed = 1.2
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (225, 0, 0)
        self.bullets_allowed = 4

