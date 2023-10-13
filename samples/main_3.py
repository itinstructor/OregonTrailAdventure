import random


class OregonTrailGame:
    def __init__(self):
        self.player_name = ""
        self.health = 100
        self.food = 100
        self.distance_traveled = 0

    def start_game(self):
        print("Welcome to the Oregon Trail Game!")
        self.player_name = input("Enter your name: ")
        print(f"Welcome, {self.player_name}! Your journey begins.")

        while self.health > 0 and self.distance_traveled < 200:
            self.show_menu()

        if self.health <= 0:
            print("Game Over! You ran out of health.")
        else:
            print("Congratulations! You've reached the end of the trail.")

    def show_menu(self):
        print("\nMain Menu:")
        print("1. Continue on the trail")
        print("2. Rest")
        print("3. Check supplies")
        choice = input("Enter your choice: ")

        if choice == "1":
            self.continue_on_trail()
        elif choice == "2":
            self.rest()
        elif choice == "3":
            self.check_supplies()
        else:
            print("Invalid choice. Try again.")

    def continue_on_trail(self):
        distance_covered = random.randint(5, 15)
        self.distance_traveled += distance_covered
        self.food -= 10
        self.health -= 5

        print(f"You traveled {distance_covered} miles.")
        print(
            f"Health: {self.health}, Food: {self.food}, Distance Traveled: {self.distance_traveled} miles")

    def rest(self):
        self.health += 20
        self.food -= 10

        print("You rested and regained some health.")
        print(f"Health: {self.health}, Food: {self.food}")

    def check_supplies(self):
        print(
            f"Health: {self.health}, Food: {self.food}, Distance Traveled: {self.distance_traveled} miles")


if __name__ == "__main__":
    game = OregonTrailGame()
    game.start_game()
