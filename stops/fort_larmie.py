"""
    Name: Fort Larmie
    File: fort_larmie.py
    Version: 1
    Description: Stop at Fort Larmie WY to recover supplies, regain health, and hunt
"""

# Import the common Stop class
# enforces inheriting the get_description and interact methods
import time
from rich.progress import Progress
from stops.stop import Stop
import stops.ascii_art
import random
import player
# Import Console for console printing
from rich.console import Console
# Import Panel for title displays
from rich.panel import Panel
# Initialize rich.console
console = Console()

class FortLarmie(Stop):
    def __init__(self, fort_larmie):
        self._fort_larmie = fort_larmie

    @property
    def stop_name(self):
        return self._fort_larmie

    #
    def get_description(self):
        """Prints a description of the current stop."""
        console.print(f"[yellow]{stops.ascii_art.fort}[/yellow]")
        console.print(f"[green]{self._fort_larmie}[/green]")
        
        desc = "\nYou've reached the mighty Fort Larmie, "
        desc += "your first stop in the great state of Wyoming. "
        desc += "It's time to resupply."
        print(desc)

    def interact(self, player):
        """
        Args:
            player (object): player object that interacts with the current stop.

        Example Usage:
            river = River()
            player = Player()
            river.interact(player)

        The code creates an instance of the `River` class
        and an instance of the `Player` class.
        It then calls the `interact` method on the `river` object,
        passing the `player` object as an argument.
        This allows the player to interact with the river in the game.
        """
        while True:
            self.get_description()
            # When concatenating a string, you must use the += operator
            menu = "What will you do?\n"
            menu += "1. Rest\n"
            menu += "2. Buy supplies\n"
            menu += "3. Go hunting\n"
            menu += "4. Continue on your journey"
            menu += "\nEnter your choice: "
            choice = input(menu)

            if choice == "1":
                """Choose to rest and recover HP"""
                print("You've laid to rest and recovered your health.")
                player.recover_health(100)

            elif choice == "2":
                # Anywhere you call a method that has a player parameter,
                # you must pass a player argument 
                # The player object is what keeps track of everything
                self.get_supplies(player)
            
            elif choice == "3":
                self.go_hunting(player)

            elif choice == "4":
                self.march_on(player)
            else:
                print("Please select one of the options!")

    def get_supplies(self, player):
        """Allows the player to shop to get more supplies for their trip"""
        while True:
            player.display_status()
            menu = "Welcome to the Fort Larmie Shop!\n"
            menu = "What would you like to purchase?\n"
            menu += "1. More Food $5\n"
            menu += "2. Winter Clothes (Increase Max HP to 200) $700\n"
            menu += "3. Bullets $1\n"
            menu += "4. Return to Fort Larmie"
            menu += "\nEnter your choice: "
            choice = input(menu)

            if choice == "1":
                """Once the player selects buy food it checks to see if they have the
                money, takes the money and adds the food."""
                player.spend_money(5)
                player.add_food(10)

            elif choice == "2":
                """If the player chooses the winter clothes I have no clue how to 
                increase the max hp so as of right now I'm glad there is no way to make money."""
                print("You can't afford that right now!")

            elif choice == "3":
                """If the player chooses to buy bullets either we can add bullets to the player
                inventory for the whole game or I'll add it here for my mini game"""
                player.spend_money(1)
                # Add bullets to the player's inventory
                player.inventory['bullets'] += 10    
            
            elif choice == "4":
                # Return player back to main menu
                self.interact(player)
            
            else:
                print("Please select one of the options!")

    def go_hunting(self, player):
        """The hunting mini game where random picks 10 random numbers 
        1-4 are misses
        4-6 are squirrels
        6-8 are rabbits
        9 are deer
        10 are buffalo"""
        if player.inventory['bullets'] < 10:
            print("You must go to the shop and buy some bullets!")
            # Return player back to main menu
            self.interact(player)
        else:
            possible_outcomes = list(range(1, 11))
            unique_outcomes = random.sample(possible_outcomes, 10)

            # Initialize variables to keep track of counts
            misses = 0
            squirrels = 0
            rabbits = 0
            deer = 0
            buffalo = 0

            for outcome in unique_outcomes:
                if 1 <= outcome <= 4:
                    print("You missed the target.")
                    misses += 1
                elif 4 < outcome <= 6:
                    print("You caught a squirrel.")
                    squirrels += 1
                    player.add_food(1)
                elif 6 < outcome <= 8:
                    print("You caught a rabbit.")
                    rabbits += 1
                    player.add_food(2)
                elif outcome == 9:
                    print("You caught a deer.")
                    deer += 1
                    player.add_food(5)
                elif outcome == 10:
                    print("You caught a buffalo.")
                    buffalo += 1
                    player.add_food(10)

            # Display the catch counts
            print("Catch Counts:")
            print(f"Misses: {misses}")
            print(f"Squirrels: {squirrels}")
            print(f"Rabbits: {rabbits}")
            print(f"Deer: {deer}")
            print(f"Buffalo: {buffalo}")
        
            # Return player back to main menu
            self.interact(player)

    def march_on(self, player):
        print("You've decided to continue on with your journey to Oregon!")
            
        # Add distance traveled to player
        player.add_distance(50)