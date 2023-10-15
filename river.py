import random
from stop import Stop  # Import the common Stop class
# import player
class River(Stop):
    def get_description(self):
        """
        Returns a description of the river.

        Returns:
            str: A string describing the river
        """
        desc = "You've reached a fast-flowing river, "
        desc += "known as the Wild River. It's too deep to ford."
        return desc

    def interact(self, player):
        print(self.get_description())
        menu = "What will you do?\n"
        menu += "1. Attempt to ford the river\n"
        menu += "2. Look for a ferry\n"
        menu += "3. Cancel and return to the main menu\nEnter your choice: "
        choice = input(menu)

        if choice == '1':
            # Implement logic for attempting to ford the river
            print("You attempt to ford the river.")
            # Check if the player successfully fords the river
            # Example: 50% chance of success
            if random.random() < 0.5:
                print("You successfully ford the river.")
            else:
                print("The river is too treacherous, you fail to cross safely.")
                player.take_damage(10)

        elif choice == '2':
            # Implement logic for looking for a ferry
            print("You decide to look for a ferry.")

        elif choice == '3':
            print("You return to the main menu.")
        else:
            print("Invalid choice. Please try again.")
