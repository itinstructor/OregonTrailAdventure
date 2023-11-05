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