"""
    Name: Kansas River Class
    File: kansas_river.py
    Version: 1
    Description: Crossing the Kansas River
    This is a template for creating other stops along the oregon trail
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


class KansasRiver(Stop):

    # --------------------- GET DESCRIPTION -----------------------------------#
    def get_description(self):
        """Prints a description of the current stop."""
        console.print(f"[blue]{stops.ascii_art.river}[/blue]")
        console.print(f"[green]{self._stop_name}[/green]")

        desc = "\nYou've reached a fast-flowing river, "
        desc += "known as the Kansas River. "
        desc += "It's too deep to ford."
        print(desc)

# ------------------------ INTERACT ---------------------------------------#
    def interact(self, player):
        """
        Allows the player to interact with the current_stop. The current_stop
        is the current stop the player is on.

        Args:
            player (object): The player object that interacts with
            the current stop.

        Returns:
            None

        Example Usage:
            current_stop = CurrentStop()
            player = Player()
            current_stop.interact(player)

        The code creates an instance of the `CurrentStop` class
        and an instance of the `Player` class.
        It then calls the `interact` method on the `CurrentStop` object,
        passing the `player` object as an argument.
        This allows the player to interact with the current_stop in the game.
        """
        # Rich Progress bar to simulate traveling through the current_stop
        with Progress() as progress:
            task1 = progress.add_task("[green]Traveling...", total=100)

            while not progress.finished:
                progress.update(task1, advance=0.5)
                time.sleep(0.02)

        self.get_description()
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
                desc = (" [bright_red]The river is too treacherous, ")
                desc += (" you fail to cross safely.[/bright_red]")
                console.print(desc)

                # Player takes damage and repeats current stop
                player.take_damage(10)
                player.current_stop -= 1

        elif choice == "2":
            """Look for a ferry"""
            print("You decide to look for a ferry.")

            # Check if the player successfully finds a ferry
            # 33% chance of success, 0, 1 or 2
            interaction = random.randint(0, 2)

            if interaction == 0:
                print(" You found a ferry and crossed the river!")

                # Add distance traveled to player
                player.add_distance(50)

            elif interaction == 1:
                print(" You did not find a ferry.")

                # Player takes damage and repeats current stop
                player.take_damage(10)
                player.current_stop -= 1

            elif interaction == 2:
                desc = " You find a ferry, fall in the river, "
                desc += " and die of dysentery."
                print(desc)
                print(stops.ascii.tombstone)
                player.take_damage(200)

        elif choice == '3':
            print("You return to the main menu.")
        else:
            print("Invalid choice. Please try again.")
