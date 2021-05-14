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
        self.ship_limit = 3

        #Bullet settings
        self.bullet_speed = 1.2
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (225, 0, 0)
        self.bullets_allowed = 4

        #Alien settings
        self.alien_speed = .2
        self.fleet_drop_speed = 10
        
        #fleet direction settings, 1 = right and -1 = left
        self.fleet_direction = 1

