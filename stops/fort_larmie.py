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
                self.get_supplies()
            
            elif choice == "3":
                self.go_hunting()

            elif choice == "4":
                self.march_on()
            else:
                print("Please select one of the options!")

    def get_supplies(self):
        """Allows the player to shop to get more supplies for his trip"""
        while True:
            menu = "Welcome to the Fort Larmie Shop!\n"
            menu = "What would you like to purchase?\n"
            menu = "1. More Food $10\n"
            menu = "2. Winter Clothes (Increase Max HP to 200) $700\n"
            menu = "3. Bullets $5\n"
            choice = input(menu)

            if choice == "1":
                
    def go_hunting(self):
        pass
    def march_on(self):
        pass