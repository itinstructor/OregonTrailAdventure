class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = {'food': 100, 'money': 500}
        self.distance_traveled = 0  # Track distance traveled

    def take_damage(self, damage):
        self.health -= damage

    def has_food(self, amount):
        return self.inventory.get('food', 0) >= amount

    def consume_food(self, amount):
        if self.has_food(amount):
            self.inventory['food'] -= amount
        else:
            self.health -= 10  # Lose health if there's not enough food

    def spend_money(self, amount):
        if self.inventory.get('money', 0) >= amount:
            self.inventory['money'] -= amount

    def display_status(self):
        print(f"{self.name}'s Status:")
        print(f"Health: {self.health}")
        print(f"Food: {self.inventory['food']}")
        print(f"Money: {self.inventory['money']}")
        print(f"Distance Traveled: {self.distance_traveled} miles")
