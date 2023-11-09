"""
    Name: Stop Class
    File: stop.py
    Version: 1
    Description: Common stop class for inheritance
    Each stop must implement these properties and Methods
    This is called an abstract class in other languages
"""


class Stop():
    def __init__(self, stop_name):
        """
        Initializes a new instance of the Stop class with 
          the given stop name.

        Args:
            stop_name (str): The name of the stop.

        Example:
            stop = Stop("River")
            print(stop.stop_name)

        Example Usage:
            river = River()

            This code creates a new instance of the Stop class called stop
            with the stop name "River".
        """
        self._stop_name = stop_name

# ---------------------------- STOP NAME ----------------------------------#
    @property
    def stop_name(self):
        return self._stop_name

# ---------------------- GET DESCRIPTION ----------------------------------#
    def get_description(self):
        """Prints a description of the current stop."""
        pass

# ---------------------------- INTERACT -----------------------------------#
    def interact(self, player):
        """
        Args:
            player (object): The player object that interacts with
              the current stop.

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
        pass
