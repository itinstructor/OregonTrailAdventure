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
from player import Player
from stops.kansas_river import River

# Windows: pip install rich
# Linux: pip3 install rich
# Import Console for console printing
from rich.console import Console
# Import Panel for title displays
from rich.panel import Panel
# Initialize rich.console
console = Console()

# Define the stops along the Oregon Trail
STOPS = [
    River("Kansas River Crossing")
]


def main_menu():
    """
    Displays the main menu for the Oregon Trail game 
    Allows the player to choose between traveling to the next stop
    checking their player status, or quitting the game.

    Inputs:
    - None

    Outputs:
    - None

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
    # This will be replaced by something cool!
    console.print(
        Panel.fit(
            " Welcome to the Oregon Trail Adventure! ",
            style="bold blue",
            subtitle="by Buddy the Cougar")
    )

# ------------------- GET PLAYER NAME -------------------------------------#
    # Initialize a player object with the player's name
    # The Player object allows us to keep the player's information
    # intact as we go from stop to stop
    player_name = Prompt.ask(" [bold green]Enter your name[/bold green]")

    # Create player object
    # Title Case The Player's Name
    player = Player(player_name.title())

# ------------------- MAIN MENU LOOP --------------------------------------#
    while player.current_stop < len(STOPS):

        console.print(
            "\n[bold green]Oregon Trail Adventure Main Menu:[/bold green]"
        )
        print(" 1. Travel to the next stop")
        print(" 2. Check player status")
        print(" 9. Quit")
        choice = input(" Enter your choice: ")

# -------------------------- TRAVEL TO NEXT STOP --------------------------#
        if choice == '1':
            # TODO: Replace with logic to determine the current stop
            # We want a data structure like a list to store the stops
            # Easily rearrange and add stops
            # Update the current stop
            current_stop = STOPS[player._current_stop]

            # current_stop = River(" Kansas River Crossing")
            # Pass instance of player to current_stop
            current_stop.interact(player)

            # Display status after stop
            print(player.display_status())

            # If a player's health is less than 0, they didn't survive
            if player.health <= 0:
                message = f"[bold red] Sorry {player.name}, "
                message += "you didn't make it."
                message += "Have a nice funeral.[/bold red]"
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
            message = f"[bold blue] Thanks for playing {player_name}. "
            message += "Goodbye![/bold blue]"
            console.print(message)
            break

        else:
            print(" Invalid choice. Please try again.")

        console.print(
            f"[bold blue] {player_name}, thanks for playing the Oregon Trail Adventure . . . Bye!"
        )


if __name__ == "__main__":
    main_menu()
