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
        self._name = name
        self._health = 100
        self._distance_traveled = 0
        # TODO: Other items can be added to the inventory
        self._inventory = {'food': 100, 'money': 500, 'bullets': 50}

        # Track which stop the player is at
        # Initialize to first stop
        self._current_stop = 0

        # TODO Other properties can be added to the player

# ------------------------ CURRENT STOP -----------------------------------#
    @property
    def current_stop(self) -> int:
        return self._current_stop

    @current_stop.setter
    def current_stop(self, stop: int):
        self._current_stop = stop
    
    @property
    def health(self)-> int:
        return self._health
    
    @health.setter
    def health(self, health: int):
        self._health = health


# ------------------------ DISTANCE TRAVELED ------------------------------#
    def add_distance(self, distance):
        """
        Increase the player's distance traveled by a specified amount.

        Parameters:
            distance (int): Distance the player has traveled.

        Returns:
            None: The method does not return any value.
            It only updates the player's health attribute.
        """
        self._distance_traveled += distance

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
        self._health -= damage

# ------------------------ RECOVER HEALTH ------------------------------------#
    def recover_health(self, recover):
        """
        Increase the player's health by a specified amount.

        Parameters:
            recover (int): The amount of health restored to the player.

        Returns:
            None: The method does not return any value.
            It only updates the player's health attribute.
        """
        self._health += recover

        """Cap the health at 100"""
        if self._health > 100:
            self._health = 100

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
        return self._inventory.get('food', 0) >= amount

# -------------------------- ADD FOOD -------------------------------------#
    def add_food(self, amount):
        """
        Adds the specified amount of food to the player's inventory.

        Args:
        amount (int): The amount of food to be added to the inventory.

        Example Usage:
        ```python
        # Create a player object
        player = Player("John")

        # Add 20 units of food to the player's inventory
        player.add_food(20)

        # Display the player's status
        player.display_status()
        ```
        Output:
        John's Status:
        Health: 100
        Food: 120
        Money: 500
        Distance Traveled: 0 miles
        """
        # Add food to the player's inventory
        self._inventory['food'] += amount

# ------------------------ CONSUME FOOD -----------------------------------#
    def consume_food(self, amount):
        """
        Consumes the specified amount of food from the player's inventory.

        If the player has enough food,
        the specified amount is subtracted from the food inventory.
        If there is not enough food, the player's health is reduced by 10.

        Args:
        amount (int): The amount of food to be consumed.

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
            # Eat food to gain health
            self._inventory['food'] -= amount
            self._health += 5
            # Cap the health at 100
            if self._health > 100:
                self._health = 100
        else:
            # Lose health if there's not enough food
            self._health -= 10

# ------------------------ SPEND MONEY -----------------------------------#
    def spend_money(self, amount):
        """
        Subtracts the specified amount from the player's
        money inventory if they have enough money.

        Parameters:
        amount (int): The amount of money to be spent.

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
        if self._inventory.get('money', 0) >= amount:
            # Subtract amount from player's money inventory
            self._inventory['money'] -= amount

# ------------------------ DISPLAY STATUS ----------------------------------#
    def display_status(self):
        """
        Prints the current status of the player.

        This method prints the player's name, health, food inventory,
        money inventory, bullet inventory and distance traveled.

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
        print(f" --------- {self._name}'s Status --------")
        print(f"   Health: {self._health}")
        print(f"     Food: {self._inventory.get('food')}")
        print(f"    Money: {self._inventory.get('money')}")
        print(f"  Bullets: {self._inventory.get('bullets')}")
        print(f" Distance: {self._distance_traveled} miles")
