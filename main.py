"""
    Name: Oregon Trail Adventure
    File: main.py
    Version: 1
    Description: Main menu for program
"""
# Import the Player class to track the players attributes
# Import other stop classes similarly
from rich.prompt import Prompt
import sys
import stops.ascii_art
from player import Player
from stops.kansas_river import KansasRiver
from stops.fort_kearney import FortKearney
from stops.north_platte_river import NorthPlatteRiver
from stops.fort_laramie import FortLaramie

# Windows: pip install rich
# Linux: pip3 install rich
# Import Console for console printing
from rich.console import Console
# Import Panel for title displays
from rich.panel import Panel
# Initialize rich.console
console = Console()

# Define the stops along the Oregon Trail
# When you are testing your stop, put it at the top of the list.
# You can move it down when you are sure it works properly.
STOPS = [
    KansasRiver("Kansas River Crossing, KS"),
    FortKearney("Fort Kearney, NE"),
    NorthPlatteRiver("North Platte River, NE"),
    FortLaramie("Fort Laramie, WY")
]


def main_menu():
    """
    Displays the main menu for the Oregon Trail game 
    Allows the player to choose between traveling to the next stop
    checking their player status, or quitting the game.

    Example Usage:
    Welcome to the Oregon Trail Game!
    Enter your name: John
    Main Menu:
    1. Travel to the next stop
    2. Check player status
    3. Quit
    Enter your choice: 1
    John has traveled 50 miles.
    John has arrived at the Wild River.
    Main Menu:
    1. Travel to the next stop
    2. Check player status
    3. Quit
    Enter your choice: 2
    Player Name: John
    Distance Traveled: 50 miles
    Main Menu:
    1. Travel to the next stop
    2. Check player status
    3. Quit
    Enter your choice: 3
    Thanks for playing. Goodbye!
    """
    console.print(f"[yellow]{stops.ascii_art.wagon}[/yellow]")
    console.print(
        Panel.fit(
            " Welcome to the Oregon Trail Adventure! ",
            style="bold blue",
            subtitle="by Buddy the Cougar")
    )
    print(" Welcome to the Oregon Trail Adventure!")
    print(" You are embarking on a journey to the west.")
    print(" Your goal is to reach Oregon safely.")
    print(" You'll face various challenges and make decisions along the way.")

# ------------------- GET PLAYER NAME -------------------------------------#
    # Initialize a player object with the player's name
    # The Player object allows us to keep the player's information
    # intact as we go from stop to stop
    player_name = Prompt.ask(" [bold green]Enter your name[/bold green]")
    player_name = player_name.title()

    # Create player object, Title Case The Player's Name
    player = Player(player_name)
    console.print(
        f" [green]Welcome {player._name} to the Oregon Trail![/green]"
    )

# ------------------- MAIN MENU LOOP --------------------------------------#
    while player.current_stop < len(STOPS):
        # TODO: Replace with logic to determine the current stop
        # We want a data structure like a list to store the stops
        # Easily rearrange and add stops
        # Update the current stop
        current_stop = STOPS[player._current_stop]

        # While the current_stop number is less than the
        # number of stops in the stops list
        print(f" 1. Travel to {current_stop.stop_name} ")
        print(" 2. Check player status")
        print(" 9. Quit")

        choice = input(" Enter your choice: ")

# -------------------------- TRAVEL TO NEXT STOP --------------------------#
        if choice == '1':
            # current_stop = River(" Kansas River Crossing")
            # Pass instance of player to current_stop
            current_stop.interact(player)

            # Display status after stop
            print(player.display_status())

            # If a player's health is less than 0, they didn't survive
            if player._health <= 0:
                message = f"[red] Sorry {player._name}, "
                message += "you didn't make it to Oregon.[/red]"
                console.print(message)

                # Exit the program, the player died
                sys.exit(0)

            # Go to the next stop
            player.current_stop += 1

# -------------------------- DISPLAY STATUS -------------------------------#
        elif choice == '2':
            player.display_status()

# -------------------------- PICKLE PLAYER STATE --------------------------#
        elif choice == '3':
            # TODO: Anyone: Pickle the player's state
            pass

# -------------------------- UNPICKLE PLAYER STATE ------------------------#
        elif choice == '4':
            # TODO: Anyone: Unpickle the player's state
            pass

# -------------------------- EXIT GAME ------------------------------------#
        elif choice == '9':
            # Exit the game
            say_goodby(player_name)
            sys.exit()

        else:
            print(" Invalid choice. Please try again.")

    # if we get killed
    # say_goodby(player_name)


def say_goodby(player_name):
    desc = f"[green]{player_name} [/green]"
    desc += "\n[blue]Thank you for playing the Oregon Trail Adventure[/blue]"
    desc += "\n[bold blue]Hasta Luego, Amigo![/bold blue]"
    console.print(desc)


if __name__ == "__main__":
    main_menu()
