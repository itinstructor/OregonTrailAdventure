"""
    Name: Stop Class
    File: stop.py
    Version: 1
    Description: Common stop class for inheritance
    Each stop must implement these methods
"""


class Stop:
    def __init__(self, stop_name):
        self._stop_name = stop_name

    @property
    def stop_name(self):
        return self._stop_name

    #
    def get_description(self):
        """Prints a description of the current stop."""
        pass

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
        pass
