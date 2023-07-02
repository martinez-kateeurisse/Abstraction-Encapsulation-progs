#Import fan class and design modules
from fan_class import Fan
from colorama import Back, Fore, Style 
from pyfiglet import Figlet

#Create a class
class UserInterface():
    #Initialize object values
    def __init__(self):
        #Fan 1 status' values
        self.fan1 = Fan(Fan.FAST, 10, "yellow", True)
        #Fan 2 status' values
        self.fan2 = Fan(Fan.MEDIUM, 5, "blue", False)

    #Defining fan 1 output
    def obj1_displays(self):
        header = Figlet(font='bubble') #For header
        title = Figlet (font = 'digital') #For titles
        info = Figlet (font = "larry3d") #For infos/ values
        fan1_status = header.renderText("FAN 1 - STATUS")
        speed_title = title.renderText("Fan Speed: ") 
        speed_info = info.renderText(str(self.fan1.get_speed())) #Fan 1 Speed
        radius_title = title.renderText("Fan Radius: ")
        radius_info = info.renderText(str(self.fan1.get_radius())) #Fan 1 Radius
        color_title = title.renderText("Fan Color: ")
        color_info = info.renderText(self.fan1.get_color()) #Fan 1 Color
        power_title = title.renderText("Fan Power")
        power_info = info.renderText("On" if self.fan1.get_power() else "Off")  #Fan 1 Power

        # Printing Fan 1 details
        print(Fore.LIGHTYELLOW_EX + fan1_status)
        print(Fore.CYAN + speed_title)
        print(Fore.LIGHTMAGENTA_EX + speed_info)        
        print(Fore.CYAN + radius_title)
        print(Fore.LIGHTMAGENTA_EX + radius_info)
        print(Fore.CYAN + color_title)
        print(Fore.LIGHTMAGENTA_EX + color_info)
        print(Fore.CYAN + power_title)
        print(Fore.LIGHTMAGENTA_EX + power_info)
    
    #Defining fan 2 output
    def obj2_displays(self):
        header = Figlet(font='bubble') #For Header
        title = Figlet (font = 'digital') #For Titles
        info = Figlet (font = "larry3d")  #For infos/values
        fan2_status = header.renderText("FAN 2 - STATUS")
        speed_title = title.renderText("Fan Speed: ")  
        speed_info = info.renderText(str(self.fan2.get_speed())) #Fan 2 Speed
        radius_title = title.renderText("Fan Radius: ")
        radius_info = info.renderText(str(self.fan2.get_radius())) #Fan 2 Radius
        color_title = title.renderText("Fan Color: ")
        color_info = info.renderText(self.fan2.get_color())  #Fan 2 Color
        power_title = title.renderText("Fan Power")
        power_info = info.renderText("On" if self.fan2.get_power() else "Off")  #Fan 2 Power

        # Printing Fan 2 details
        print(Fore.LIGHTYELLOW_EX + fan2_status)
        print(Fore.CYAN + speed_title)
        print(Fore.LIGHTMAGENTA_EX + speed_info)        
        print(Fore.CYAN + radius_title)
        print(Fore.LIGHTMAGENTA_EX + radius_info)
        print(Fore.CYAN + color_title)
        print(Fore.LIGHTMAGENTA_EX + color_info)
        print(Fore.CYAN + power_title)
        print(Fore.LIGHTMAGENTA_EX + power_info)