from player import Player
from river import River  # Import other stop classes similarly


def main_menu():
    print("Welcome to the Oregon Trail Game!")
    player_name = input("Enter your name: ")
    player = Player(player_name)

    while True:
        print("\nMain Menu:")
        print("1. Travel to the next stop")
        print("2. Check player status")
        print("3. Quit")
        choice = input("Enter your choice: ")

        if choice == '1':
            player.distance_traveled += 50  # Simulated distance traveled
            # Replace with logic to determine the current stop
            current_stop = River("Wild River")
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
