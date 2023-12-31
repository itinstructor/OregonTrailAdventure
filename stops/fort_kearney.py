# Import the common Stop class
# enforces inheriting the get_description and interact methods
from stops.stop import Stop
import stops.ascii_art
import random
# Import Console for console printing
from rich.console import Console
# Import Panel for title displays
from rich.panel import Panel
# Initialize rich.console
console = Console()


class FortKearney(Stop):
    # --------------------- GET DESCRIPTION -----------------------------------#
    def get_description(self):
        """Prints a description of the current stop."""
        console.print(f"[green]{self.stop_name}[/green]")

        desc = "\nYou've reached an open prairie, "
        desc += "it's covered in lush grassland and beautiful flowers. "
        desc += "Off in the distance you also spot... wait... BUFFALO?"
        return desc

# ----------------------- INTERACT ----------------------------------------#
    def interact(self, player):
        """
        Allows the player to interact with the grassland and choose to hunt buffalo 

        Args:
            player (object): The player object that interacts with the prairie

        Example Usage:
            prarie = Prairie()
            player = Player()
            prarie.interact(player)
        """
        # Simulated distance traveled
        player.distance_traveled += 50
        print(self.get_description())
        menu = "What will you do?\n\n"
        menu += "1. Take a respite and gaze upon the beauty of the Buffalo\n"
        menu += "2. Hunt a few buffalo for food\n"
        menu += "3. Hunt all the buffalo because your dark desires tell you to >:)\n"
        menu += "4. Return to menu\n"
        menu += "\nEnter your choice: "
        choice = input(menu)

        # Relax
        if choice == '1':

            print("\nYou sit down, surrounded by the luscious nature around you.")

            # See if the buffalo notice you

            # Example: 50% chance of success, 0 or 1
            interaction = random.randint(0, 1)
            if interaction == 0:
                print("The herd of bison seem to not notice you.")

            elif interaction == 1:
                desc = """
The herd of bison seem to think you're trying to eat their delicious grass.
One member of the herd comes over and rams you off their turf (-15 HP)
"""
                print(desc)
                player.take_damage(15)

        # Hunt for bison
        elif choice == '2':
            # Hunt for a few bison
            print("You grab your hunting rifle and shoot at a few of the bison.")

            # Chance
            interaction = random.randint(0, 1)
            if interaction == 0:
                print("You successfully brought down two bison!")
                player.inventory["food"] += 200

            else:
                desc = """
You missed all of your shots and the herd ran away
(you really need to work on your aim!)
"""

        # K I L L  T H E M  A L L
        elif choice == "3":

            # Let user affirm that they want to do this
            choice = input("""\nWait really? 
There's like 40 Bison in this herd!
At most, you'll only be able to carry 3 of them with you for food!
Are you sure you want to do this? [Y/N]: """
                           ).lower()

            # Yes
            if choice == "y":
                desc = """
You grab your hunting rifle and mow down the herd.
How you were able to mow down 40 bison with a 19th century rifle is beyond me,
but you somehow did.
Congrats (You monster...)
"""
                player.inventory["food"] = 200
            # No
            else:
                print("That's probably for the best.")
                self.interact(player)

        # Return main menu
        elif choice == '4':
            print("You return to the main menu.")

        # Error
        else:
            print("Invalid choice. Please try again.")
