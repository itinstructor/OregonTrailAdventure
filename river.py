"""
    Name: River Class
    File: player.py
    Version: 1
    Description: Crossing the North Platte River
"""
import random
# Import the common Stop class
# enforces inheriting the get_description and interact methods
from stop import Stop


class River(Stop):
    def get_description(self):
        """
        Returns a description of the river.

        Returns:
            str: A string describing the river
        """
        desc = "You've reached a fast-flowing river, "
        desc += "known as the Wild North Platte River. "
        desc +=  "It's too deep to ford."
        return desc

    def interact(self, player):
        """
        Allows the player to interact with the river in a text-based game.

        Args:
            player (object): The player object that interacts with the river.

        Returns:
            None

        Raises:
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
        player.distance_traveled += 50
        print(self.get_description())
        menu = "What will you do?\n"
        menu += "1. Attempt to ford the river\n"
        menu += "2. Look for a ferry\n"
        menu += "3. Cancel and return to the main menu"
        menu += "\nEnter your choice: "
        choice = input(menu)

        if choice == '1':
            # Implement logic for attempting to ford the river
            print("You attempt to ford the river.")
            # Check if the player successfully fords the river
            # Example: 50% chance of success, 0 or 1
            interaction = random.randint(0, 1)
            if interaction == 0:
                print("You successfully ford the river.")
            elif interaction == 1:
                print("The river is too treacherous, you fail to cross safely.")
                player.take_damage(10)

        elif choice == '2':
            # Implement logic for looking for a ferry
            print("You decide to look for a ferry.")

        elif choice == '3':
            print("You return to the main menu.")
        else:
            print("Invalid choice. Please try again.")
