"""
    Name: Kansas River Class
    File: kansas_river.py
    Version: 1
    Description: Crossing the Kansas River
    This is a template for creating other stops along the oregon trail
"""
import random
# Import the common Stop class
# enforces inheriting the get_description and interact methods
from stops.stop import Stop
import stops.ascii_art


class NorthPlatteRiver(Stop):

    def __init__(self, stop_name):
        self.stop_name = stop_name

    def get_description(self):
        """
        Returns a description of the river.

        Returns:
            str: A string describing the river
        """
        desc = stops.ascii_art.river
        desc += self.stop_name
        desc += "\nYou've reached a fast-flowing river, "
        desc += "known as the North Platte River. "
        desc += "It's too fast and deep to ford."
        return desc

    def interact(self, player):
        """
        Allows the player to interact with the river in a text-based game.

        Args:
            player (object): The player object that interacts with the river.

        Returns:
            None

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
        # Simulated distance traveled
        print(self.get_description())
        menu = "What will you do?\n"
        menu += "1. Attempt to ford the river\n"
        menu += "2. Look for a ferry\n"
        menu += "3. Cancel and return to the main menu"
        menu += "\nEnter your choice: "
        choice = input(menu)

        if choice == "1":
            """ Attempt to ford the river """
            print(" You attempt to ford the river.")

            # Check if the player successfully fords the river
            # Example: 50% chance of success, 0 or 1
            interaction = random.randint(0, 1)

            if interaction == 0:
                print(" You successfully ford the river.")
                # Add distance traveled
                player.add_distance(50)

            elif interaction == 1:
                print(" The river is too treacherous, you fail to cross safely and drown.")
                player.take_damage(100)

        elif choice == "2":
            """ Look for a ferry """
            print("You decide to look for a ferry.")

            # Check if the player successfully finds a ferry
            # Example: 50% chance of success, 0 or 1
            interaction = random.randint(0, 2)

            if interaction == 0:
                print(" You found a ferry and crossed the river!")
                # Add distance traveled
                player.add_distance(50)

            elif interaction == 1:
                print(" You did not find a ferry.")
                player.take_damage(10)

            elif interaction == 2:
                print(" You find a ferry, fall in the river, and die of dysentery.")
                player.take_damage(100)

        elif choice == '3':
            print("You return to the main menu.")
        else:
            print("Invalid choice. Please try again.")
