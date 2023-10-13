from stop import Stop  # Import the common Stop class


class River(Stop):
    def get_description(self):
        return f"You've reached a fast-flowing river, known as the Wild River. It's too deep to ford."

    def interact(self, player):
        print(self.get_description())
        choice = input(
            "What will you do?\n1. Attempt to ford the river\n2. Look for a ferry\n3. Cancel and return to the main menu\nEnter your choice: ")

        if choice == '1':
            # Implement logic for attempting to ford the river
            pass
        elif choice == '2':
            # Implement logic for looking for a ferry
            pass
        elif choice == '3':
            print("You return to the main menu.")
        else:
            print("Invalid choice. Please try again.")
