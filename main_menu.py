"""
    Name: Oregon Trail Adventure
    File: main_menu.py
    Version: 1
    Description: Main menu for program
"""

# Import the Player class to track the players attributes
from player import Player
from river import River  # Import other stop classes similarly


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

    print("Welcome to the Oregon Trail Adventure!")

    # Initialize a player object with the player's name
    # The Player object allows us to keep the player's information
    # intact as we go from object to object
    player_name = input("Enter your name: ")
    player = Player(player_name)

    while True:
        print("\nMain Menu:")
        print("1. Travel to the next stop")
        print("2. Check player status")
        print("3. Quit")
        choice = input("Enter your choice: ")

        if choice == '1':
            # Simulated distance traveled
            player.distance_traveled += 50
            # Replace with logic to determine the current stop
            current_stop = River("Wild River")
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
