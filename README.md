# OregonTrailGPT
Practice GitHub using ChatGPT and shared coding

Gus Allred is here.
Collaborators:
1. Aidan Newberry (regtoga)
2. Arturo Montiel (Montiel8)
3. Yonatan Getachew (Yogetachew)
4. Josiah Andrews (siahdrews)

# Story
Imagine you're going on a long adventure, like a big trip. In this game, you need to be healthy and travel a long distance. You start with 100 points of health. The goal is to travel 1000 miles without losing all your health.

You have three things you can do:

1. **Continue on your journey**: This means you keep going forward on your adventure. Sometimes, you'll travel a little, but it might make you a bit less healthy.

2. **Rest**: This is like taking a break. It helps you feel better and become healthier.

3. **Quit**: If you want to stop the game, you can choose to quit.

Your job is to make choices and try to travel the whole 1000 miles without running out of health. If you run out of health, you lose the game. If you make it to 1000 miles with some health left, you win!

So, just remember, keep an eye on your health, make choices, and try to go on this adventure as far as you can. Good luck!

# Plan of Attack
Certainly, let's create a simple text-based "Oregon Trail" game in Python with a command-line interface. In this game, travelers will make choices as they embark on their journey. We'll create a basic structure with a `main.py` as the menu system and six separate class files for different stops along the way. Here's an overview:

1. Create a folder for your project and place the following Python files inside it:

   - `main.py` (for the game menu)
   - `start.py` (the starting location)
   - `river.py` (river crossing location)
   - `desert.py` (desert location)
   - `forest.py` (forest location)
   - `mountains.py` (mountains location)
   - `end.py` (ending location)

2. Here's a simplified structure for `main.py`:

```python
class OregonTrailGame:
    def __init__(self):
        self.current_location = None

    def start_game(self):
        print("Welcome to the Oregon Trail!")
        self.current_location = StartLocation(self)

    def change_location(self, new_location):
        self.current_location = new_location
        self.current_location.enter()

if __name__ == "__main__":
    game = OregonTrailGame()
    game.start_game()
```

3. For the class files (e.g., `start.py`), you can structure them like this:

```python
class StartLocation:
    def __init__(self, game):
        self.game = game

    def enter(self):
        print("You are at the starting point of your journey.")

        while True:
            choice = input("What would you like to do? (1. Continue, 2. Quit): ")
            if choice == '1':
                self.game.change_location(RiverLocation(self.game))
            elif choice == '2':
                self.game.change_location(EndLocation(self.game))
            else:
                print("Invalid choice. Please enter 1 or 2.")

# Repeat a similar structure for other location classes.
```

4. Continue this structure for the river, desert, forest, mountains, and end locations, each offering different choices and consequences.

5. Ensure that when a location class is entered, it should prompt the user for their next move and handle the logic for changing the current location.

6. Once you've created all location classes and connected them through the game menu in `main.py`, players can navigate through the game by making choices and progressing through the locations.

This is a basic outline for your Oregon Trail game in Python. You can expand and customize it by adding more details, challenges, and interactions at each location. Make sure to handle game over conditions and keep track of the player's progress throughout the journey.