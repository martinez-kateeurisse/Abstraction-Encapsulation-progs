#Importing color module
from colorama import Back, Fore, Style 

#Create Class
class ProgramDesign():
    #Programs' headers
    # Car class program header
    def car_header (self):
        print(Fore.LIGHTRED_EX, """
                                   ⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣤⣴⣶⣶⣿⠿⠿⠿⢿⣶⣶⣤⣀⣀⣀⣠⣤⣤⣦⠀⠀
                                   ⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣿⡿⠿⠛⠛⠉⠉⠀⠀⠀⠀⠀⠈⢿⡏⠉⢻⣿⣿⣿⣿⣿⡆⠀
                                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⠋⠀⠀⠀⣴⣶⡄⠀⠀⢰⣿⠀⠀⠀⠘⣷⡀⠀⢹⣿⣿⣿⣿⣿⠀
                                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⣇⣀⣤⣤⣤⣾⣿⣶⣶⣶⣿⣿⣿⣿⣿⣿⣿⣷⣾⣿⣿⣿⣿⣿⣿⡆
                                     ⠀⠀⣠⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠛⠉⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃
                                    ⠀⣰⠋⠛⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣏⣁⣀⣠⣤⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀
                                    ⣰⣷⣦⣤⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠟⠛⣿⣿⣿⣿⣿⣿⣿⠁⠈⠙⢿⣿⣿⣿⣿⠀⣿⠀
                                    ⣿⣿⣿⣿⣿⣷⡀⠀⠈⠉⠉⠉⠉⠁⠀⠀⠀⠀⢀⣼⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠘⣿⣿⣿⣿⠀⣿⠀
                                    ⣿⣿⣿⣿⣿⣿⣷⣤⣀⣀⣀⣀⣀⣀⣀⣠⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⢀⣿⣿⣿⣿⣀⣿⠀
                                    ⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⢀⣼⣿⠛⠛⠛⠛⠃⠀
                                    ⠀⠈⠙⠻⢿⣿⣿⣿⠿⠟⠛⠛⠛⠛⠛⠉⠉⠉⠉⠉⠀⠈⠻⣿⣿⣿⣷⣶⣶⣿⡿⠁⠀⠀⠀⠀⠀⠀
                                      ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  ⠀⠀⠀⠀⠈⠉⠉⠉⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀"""+ Fore.LIGHTYELLOW_EX,"""                      
                                       
                                      ▄▄ █▀▀ ▄▀█ █▀█   █▀▀ █░░ ▄▀█ █▀ █▀ ▄▄
                                      ░░ █▄▄ █▀█ █▀▄   █▄▄ █▄▄ █▀█ ▄█ ▄█ ░░""")
        print(Fore.WHITE,  "="* 35 + "Abstraction and Encapsulation - Program 2" + "="* 35 ,"\n\n")

    # Fan class Program Header
    def fan_header (self):
        print(Fore.LIGHTCYAN_EX, """
      ░                                       ░           ░░░█▄---------------------
                        ░               ░           ░     ░ ░░████▄▄▄▄-----------------------     ------  
            ░                                             ░░░██▀▀░░░░█----------------------
                                ░              ░          ░░ ░▀░░▓▓▓▓▀------------------------------------
                  ░                      ░                ░░░░░▄██████▄
"""+ Fore.LIGHTYELLOW_EX,"""                                       █▀▀ ▄▀█ █▄░█   █▀▀ █░░ ▄▀█ █▀ █▀
                                        █▀░ █▀█ █░▀█   █▄▄ █▄▄ █▀█ ▄█ ▄█""")
        print(Fore.WHITE,  "="* 35 + "Abstraction and Encapsulation - Program 1" + "="* 35 ,"\n\n")
    
    # Pet class Program Header
    def pet_header (self):
            print(Fore.LIGHTYELLOW_EX, """
                                             ──────▄▀▄─────▄▀▄
                                             ─────▄█░░▀▀▀▀▀░░█▄ 
                                             ─▄▄──█░░░░░░░░░░░█──▄▄
                                             █▄▄█─█░░▀░░┬░░▀░░█─█▄▄█"""+ Fore.LIGHTCYAN_EX,"""                                                      
                                         █▀█ █▀▀ ▀█▀   █▀▀ █░░ ▄▀█ █▀ █▀
                                         █▀▀ ██▄ ░█░   █▄▄ █▄▄ █▀█ ▄█ ▄█""")
            print(Fore.WHITE,  "="* 35 + "Abstraction and Encapsulation - Program 3" + "="* 35 ,"\n\n")
    
    #Program Footer
    def program_footer(self):
        print(Fore.RED, """

                                        ▀█▀ █░█ ▄▀█ █▄░█ █▄▀   █▄█ █▀█ █░█ █
                                        ░█░ █▀█ █▀█ █░▀█ █░█   ░█░ █▄█ █▄█ ▄""" + Fore.WHITE, """
                                                -🅗🅐🅥🅔 🅐 🅖🅡🅔🅐🅣 🅓🅐🅨-""")
    def loading_bar(self):
        from tqdm import tqdm
        from time import sleep
        print("LOADING PROGRAM")
        for i in tqdm(range(50)):
            sleep(0.05)
    
    def details_loading(self):
        from tqdm import tqdm
        import time

        # Set the total number of iterations for the loading bar
        total_iterations = 3

        # Define the ASCII art for the cat
        cat = r'''
        /\_/\  
        ( o.o ) 
        > ^ <
        '''
        # Create a loop using tqdm to track the progress
        for i in tqdm(range(total_iterations), desc="Loading", unit="iteration"):
            # Simulate some work being done
            time.sleep(0.1)

            # Clear the previous line and print the cat
            print('\033[F' + cat)
pd = ProgramDesign()
pd.details_loading()