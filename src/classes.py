from random import choice
from os import system, name
from time import sleep
from simple_term_menu import TerminalMenu

# Player Class for inidividual human players

class Player():
    def __init__(self, name = "undefined", health = 200, body_type = "undefined", arm_weapon = "undefined"):
        self.__name = name
        self.__health = health
        self.__body_type = body_type
        self.__arm_weapon = arm_weapon

    # Currently using
    def get_name(self):
       return self.__name

    def get_health(self):
       return self.__health

    def get_body_type(self):
        return self.__body_type
    # Currently using
    def set_name(self, name):
        self.__name = name
    # Currently using
    def set_body_type(self, body_type):
        self.__body_type = body_type

    def set_arm_weapon(self, arm_weapon):
        self.__arm_weapon = arm_weapon


# Child Class of the Player Class for AI specifics

class ComputerPlayer(Player):

    # Random names for AI player
    bot_names = ["Terminator", "Annihilator", "Destroyer", "Crusher", "Nuts-n-Bolts", "Link",
    "Mechanicus", "Ripper", "Tank", "Shredder"]
    # Added private variable name here to prevent potential access to this random name variable

    def __init__(self):
        self.__name = choice(ComputerPlayer.bot_names)
        super().__init__(self.__name)





class Game():
    # Flag var used in gamemodes to exit game CURRENTLY DON'T NEED
    flag = False
    def __init__(self):
        self.player_one = Player()
        self.player_two = Player()
        self.bot_one = ComputerPlayer()

    # DO TIME PERMITTING
    def introduction(self):
        ### Add cool ASCII Picture
        ### Add ... initializing Battle Bots ... print message
        ### Add timer pause before menu opens
        pass

    # Method that clears the terminal throughout the game so players don't have to scroll
    def clear_terminal(self):
        system("cls" if name == "nt" else "clear")

    def game_mode(self):
        self.clear_terminal()
        options = ["Single Player", "Multi Player", "Exit Game"]
        terminal_menu = TerminalMenu(options)
        menu_entry_index = terminal_menu.show()
        print(f"You have selected {options[menu_entry_index]}!\n")
        while menu_entry_index != 2:
            if menu_entry_index == 0:
                self.single_player_mode()
                self.body_type()
            elif menu_entry_index == 1:
                pass
                # DO TIME PERMITTING
                # self.multi_player_mode()
            menu_entry_index = terminal_menu.show()


    def battle(self):
        pass

    def single_player_mode(self):
        # ERORR HANDLE INPUT HERE
        self.player_one.set_name(input("What's you're Battle Robots Name ? ")) 
        print(f"\n Welcome, {self.player_one.get_name()}")
        bot = self.bot_one
        print(f"\n You're Battling: {self.bot_one.get_name()}!\n")
        print("...initializing...")
        sleep(4)
        self.clear_terminal()


    def body_type(self):
        print("Please select what body-type you want:\n")
        body_type_options = ["Tracked", "Soft-Wheeled", "Hard-Wheeled", "Exit Menu"]
        terminal_menu = TerminalMenu(body_type_options)
        menu_entry_index = terminal_menu.show()
        print(f"You have selected {body_type_options[menu_entry_index]}!\n")
        while menu_entry_index != 3:
            if menu_entry_index == 0:
                self.player_one.set_body_type("Tracked")
                break
            elif menu_entry_index == 1:
                self.player_one.set_body_type("Soft-Wheeled")
                break
            elif menu_entry_index == 2:
                self.player_one.set_body_type("Hard-Wheeled")
                break
            menu_entry_index = terminal_menu.show()