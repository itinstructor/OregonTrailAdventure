"""
    Name: Player Class
    File: player.py
    Version: 1
    Description: Player class to store attributes and methods for the player
"""


class Player:
    def __init__(self, name):
        """
        Initialize player object and properties.

        Parameters:
            name (str): The name of the player.

        Attributes:
            name (str): The name of the player.
            health (int): The health of the player, set to 100 by default.
            inventory (dict): The player's inventory,
                with initial values of 100 for food and 500 for money.
            distance_traveled (int): The distance traveled
                by the player, set to 0 by default.
        """
        self.name = name
        self.health = 100
        self.inventory = {'food': 100, 'money': 500}
        self.distance_traveled = 0
        # TODO: track which stop the player is at
        # This will allow us to pickle and unpickle the player's object

# ------------------------ TAKE DAMAGE ------------------------------------#
    def take_damage(self, damage):
        """
        Reduce the player's health by a specified amount.

        Parameters:
            damage (int): The amount of damage to be taken by the player.

        Returns:
            None: The method does not return any value.
            It only updates the player's health attribute.
        """
        self.health -= damage

# ------------------------ HAS FOOD ---------------------------------------#
    def has_food(self, amount):
        """
        Check if the player has enough food in their inventory.

        Parameters:
            amount (int): Amount of food to check for in the
            player's inventory.

        Return:
            True if the player has enough food, False otherwise.
            Type: bool
        """
        return self.inventory.get('food', 0) >= amount

# ------------------------ CONSUME FOOD -----------------------------------#
    def consume_food(self, amount):
        """
        Consumes the specified amount of food from the player's inventory.

        If the player has enough food,
        the specified amount is subtracted from the food inventory.
        If there is not enough food, the player's health is reduced by 10.

        Args:
        amount (int): The amount of food to be consumed.

        Returns:
        None

        Example Usage:
        ```python
        # Create a player object
        player = Player("John")

        # Check if the player has enough food
        if player.has_food(5):
            # Consume 5 units of food
            player.consume_food(5)
        else:
            # Reduce health by 10 if there's not enough food
            player.consume_food(0)

        # Display the player's status
        player.display_status()
        ```
        Output:
        John's Status:
        Health: 100
        Food: 95
        Money: 500
        Distance Traveled: 0 miles
        """
        if self.has_food(amount):
            # Eat food
            self.inventory['food'] -= amount
        else:
            # Lose health if there's not enough food
            self.health -= 10

# ------------------------ SPEND MOINEY -----------------------------------#
    def spend_money(self, amount):
        """
        Subtracts the specified amount from the player's
        money inventory if they have enough money.

        Parameters:
        amount (int): The amount of money to be spent.

        Returns:
        None

        Example Usage:
        ```python
        # Create a player object
        player = Player("John")

        # Spend 100 units of money
        player.spend_money(100)

        # Display the player's status
        player.display_status()
        ```
        Output:
        John's Status:
        Health: 100
        Food: 100
        Money: 400
        Distance Traveled: 0 miles
        """
        if self.inventory.get('money', 0) >= amount:
            # Subtract amount from player's money inventory
            self.inventory['money'] -= amount

# ------------------------ DISPLAY STATUS ----------------------------------#
    def display_status(self):
        """
        Prints the current status of the player.

        This method prints the player's name, health, food inventory,
        money inventory, and distance traveled.

        Example Usage:
        ```python
        # Create a player object
        player = Player("John")

        # Display the player's status
        player.display_status()
        ```
        Output:
        John's Status:
        Health: 100
        Food: 100
        Money: 500
        Distance Traveled: 0 miles
        """
        print(f"{self.name}'s Status:")
        print(f"Health: {self.health}")
        print(f"Food: {self.inventory['food']}")
        print(f"Money: {self.inventory['money']}")
        print(f"Distance Traveled: {self.distance_traveled} miles")