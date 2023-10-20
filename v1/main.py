"""
    Name: Oregon Trail Adventure
    File: main.py
    Version: 1
    Description: Main menu for program
"""

# Import the Player class to track the players attributes
from player import Player
# Import other stop classes similarly
from river import River


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
    print("Welcome to the Oregon Trail Adventure!")

    # Initialize a player object with the player's name
    # The Player object allows us to keep the player's information
    # intact as we go from object to object
    player_name = input("Enter your name: ")
    player = Player(player_name)

    # TODO: Anyone: Pickle and unpickle the player's state
    # to allow stop and start of play
    # Keep track of which stop they are on

    while True:
        print("\nMain Menu:")
        print("1. Travel to the next stop")
        print("2. Check player status")
        print("3. Quit")
        choice = input("Enter your choice: ")

        if choice == '1':
            # TODO: Replace with logic to determine the current stop
            # We want a data structure like a list to store the stops
            # Easily rearrange and add stops
            # Go from one stop to the next when the player
            # leaves the stop class
            # We don't want the stop hardcoded
            current_stop = River("Wild North Platte River")
            # Pass instance of player to current_stop
            current_stop.interact(player)

        elif choice == '2':
            player.display_status()

        elif choice == '3':
            print("Thanks for playing. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main_menu()
