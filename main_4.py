class Player:
    def __init__(self):
        self.health = 100
        self.inventory = []

    def is_game_over(self):
        return self.health <= 0


class Room:
    def __init__(self, player):
        self.player = player

    def describe(self):
        pass

    def handle_input(self):
        pass


class StartRoom(Room):
    def describe(self):
        print("You stand at the beginning of the Oregon Trail adventure. The sun is shining, and you have a sense of excitement in the air. You see your trusty covered wagon ready for the journey ahead.")

    def handle_input(self):
        while True:
            print("\nOptions:")
            print("1. Check your supplies")
            print("2. Begin your journey")
            print("3. Quit the game")

            choice = input("Enter your choice (1/2/3): ")

            if choice == '1':
                self.check_supplies()
            elif choice == '2':
                print("You embark on your journey!")
                return RiverCrossingRoom(self.player)
            elif choice == '3':
                print("You have decided to quit the game. Goodbye!")
                exit()
            else:
                print("Invalid choice. Please select a valid option.")

    def check_supplies(self):
        print("You check your supplies:")
        print(f"Health: {self.player.health}")
        print(f"Inventory: {', '.join(self.player.inventory)}")


class RiverCrossingRoom(Room):
    def describe(self):
        print("You have reached a fast-flowing river. The water looks treacherous. You need to decide how to cross.")

    def handle_input(self):
        while True:
            print("\nOptions:")
            print("1. Attempt to ford the river")
            print("2. Look for a bridge")
            print("3. Go back to the starting point")

            choice = input("Enter your choice (1/2/3): ")

            if choice == '1':
                print("You attempt to ford the river...")
                # Implement river crossing logic, modify player health, and possibly transition to other rooms
                # For simplicity, we transition to the final destination here.
                return FinalDestinationRoom(self.player)
            elif choice == '2':
                print("You search for a bridge...")
                # Implement bridge search logic and modify player health if needed
            elif choice == '3':
                print("You decide to go back to the starting point.")
                return StartRoom(self.player)
            else:
                print("Invalid choice. Please select a valid option.")


class FinalDestinationRoom(Room):
    def describe(self):
        print("Congratulations! You've reached the final destination. Your Oregon Trail adventure is a success!")

    def handle_input(self):
        print("The game is over. Thanks for playing!")
        exit()


if __name__ == "__main__":
    player = Player()
    current_room = StartRoom(player)

    print("Welcome to the Oregon Trail Adventure!")
    while not player.is_game_over():
        current_room.describe()
        current_room = current_room.handle_input()
