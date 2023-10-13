import random

# Create a class for the Oregon Trail game


class OregonTrailGame:
    def __init__(self):
        # Initialize the game with stops and the current stop
        self.stops = ["Independence", "Kansas River", "Fort Kearny",
                      "Chimney Rock", "Fort Laramie", "Oregon City"]
        self.current_stop = 0
        self.player_name = ""

    # Start the game
    def start(self):
        print("Welcome to the Oregon Trail Game!")
        self.player_name = input("Enter your name: ")

        # Continue the game until all stops are reached
        while self.current_stop < len(self.stops):
            self.show_menu()
            choice = input("Enter your choice: ")
            if choice == '1':
                self.travel()
            elif choice == '2':
                self.status()
            elif choice == '3':
                self.quit_game()
                break
            else:
                print("Invalid choice. Please try again.")

        print(
            f"Congratulations, {self.player_name}! You've reached Oregon City.")

    # Show the in-game menu
    def show_menu(self):
        print("\nCurrent Location:", self.stops[self.current_stop])
        print("1. Travel to the next stop")
        print("2. Check status")
        print("3. Quit the game")

    # Simulate traveling to the next stop
    def travel(self):
        if self.current_stop < len(self.stops) - 1:
            self.current_stop += 1
            print(f"You've traveled to {self.stops[self.current_stop]}.")
            self.random_event()

    # Display the player's current status
    def status(self):
        print(f"\nStatus for {self.player_name}:")
        print(f"Current Location: {self.stops[self.current_stop]}")
        print("Health: Good")
        print("Supplies: Adequate")
        print("Cash: $1000")

    # Simulate random events during travel
    def random_event(self):
        event = random.choice(
            ["Good weather", "Heavy rainstorm", "Illness", "Bandits"])
        if event == "Good weather":
            print("You had a smooth journey with good weather.")
        elif event == "Heavy rainstorm":
            print("Your journey was delayed due to a heavy rainstorm.")
        elif event == "Illness":
            print("One of your team members fell ill. You spent extra on medicine.")
        else:
            print("Bandits attacked your group. You lost some supplies.")

    # Quit the game
    def quit_game(self):
        print("Thanks for playing the Oregon Trail Game!")
        print("See you next time.")


# Main part of the code
if __name__ == "__main__":
    game = OregonTrailGame()  # Create an instance of the game
    game.start()  # Start the game
