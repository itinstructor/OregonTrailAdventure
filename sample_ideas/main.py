import random

# Define the main game class
class OregonTrailGame:
    def __init__(self):
        # Initialize the player's health and distance traveled
        self.health = 100
        self.distance_traveled = 0

    # Start the game
    def start_game(self):
        print("Welcome to the Oregon Trail!")
        input("Press Enter to begin your journey...")

        # Continue the game while health is above 0 and distance traveled is less than 1000 miles
        while self.health > 0 and self.distance_traveled < 1000:
            self.travel_menu()
        
        # Game ending conditions
        if self.health <= 0:
            print("Game Over. You have run out of health.")
        else:
            print("Congratulations! You have successfully completed the journey.")

    # Menu for traveling, resting, and quitting
    def travel_menu(self):
        print("\nOregon Trail - Your Stats:")
        print(f"Health: {self.health}")
        print(f"Distance Traveled: {self.distance_traveled} miles")
        print("\nWhat would you like to do?")
        print("1. Continue on your journey")
        print("2. Rest")
        print("3. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            self.continue_journey()
        elif choice == "2":
            self.rest()
        elif choice == "3":
            self.quit_game()
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

    # Logic for continuing the journey
    def continue_journey(self):
        miles = random.randint(50, 100)
        self.distance_traveled += miles
        self.health -= random.randint(5, 15)
        print(f"You have traveled {miles} miles.")
        input("Press Enter to continue...")

    # Logic for resting
    def rest(self):
        self.health += random.randint(10, 20)
        print("You have rested and regained some health.")
        input("Press Enter to continue...")

    # Logic for quitting the game
    def quit_game(self):
        print("You have quit the game.")
        self.health = 0  # End the game

# Main entry point
if __name__ == "__main__":
    game = OregonTrailGame()
    game.start_game()
