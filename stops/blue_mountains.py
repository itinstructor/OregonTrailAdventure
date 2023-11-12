"""
    Name: Blue Mountains Class
    File: blue_mountains.py
    Version: 1
"""
# Import the common Stop class
# enforces inheriting the get_description and interact methods
# Import the common Stop class
from stops.stop import Stop

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


class BlueMountains(Stop):
    def __init__(self, blue_montains):
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
        self._stop_name = blue_montains

# ---------------------------- STOP NAME ----------------------------------#
    @property
    def stop_name(self):
        return self._stop_name

# ---------------------- GET DESCRIPTION ----------------------------------#
    def get_description(self):
        """Print a description of the Blue Mountains stop."""
        description = (
            "You have reached the Blue Mountains. \nThese towering peaks "
            "are a formidable obstacle on your journey. \nThe Blue Mountains "
            "are known for their rugged terrain and unpredictable weather."
        )
        console.print(Panel.fit(description, title="Blue Mountains"))

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
        """
        Allows the player to interact with the Blue Mountains stop.

        Args:
            player (object): The player object.
        """
        console.print("You are now at the Blue Mountains.")
        console.print("What would you like to do?")
        choice = console.input(
            "[bold]'1' Rest  '2' Continue  '3' Hunt  '4' Check Supplies[/bold]"
        )

        if choice == "1":
            desc = "You decide to rest at the Blue Mountains."
            desc += "It's a wise choice to recover your strength."
            print(desc)

            # Add health, stay at current stop
            player.health += 20
            player.current_stop -= 1

        elif choice == "2":
            console.print(
                "You choose to continue your journey through the challenging Blue Mountains."
            )
            # Implement the continuation of the journey, possibly with challenges and events.

        elif choice == "3":
            console.print("You go hunting for food in the Blue Mountains.")
            # Implement hunting functionality here, e.g., gather resources, encounter wildlife, etc.

        elif choice == "4":
            console.print("You check your supplies and equipment.")
            player.display_status()

        else:
            desc = "Invalid choice. Please select a valid option: "
            desc += "'1' Rest  '2' Continue  '3' Hunt  '4' Check Supplies."
            print(desc)
