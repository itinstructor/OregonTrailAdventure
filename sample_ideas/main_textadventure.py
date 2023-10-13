import random

# Function to simulate a decision in the game


def make_decision():
    return random.choice([True, False])

# Main game loop


def oregon_trail_game():
    print("Welcome to the Oregon Trail Adventure!")
    print("You are embarking on a journey to the west. Your goal is to reach Oregon safely.")
    print("You'll face various challenges and make decisions along the way.")

    miles_traveled = 0
    food = 500
    health = 100
    weather = ['Sunny', 'Rainy', 'Snowy', 'Windy']
    distance_to_oregon = 2000
    while miles_traveled < distance_to_oregon and health > 0:
        print("\nMiles traveled: " + str(miles_traveled))
        print("Food remaining: " + str(food) + " lbs")
        print("Health: " + str(health))
        print("Weather: " + random.choice(weather))

        decision = input(
            "Do you want to (1) Continue on the trail, (2) Rest, or (3) Hunt for food? Enter the number: ")

        if decision == '1':
            miles = random.randint(50, 100)
            miles_traveled += miles
            food -= random.randint(10, 20)
            health -= random.randint(5, 15)
        elif decision == '2':
            health += random.randint(10, 20)
        elif decision == '3':
            food += random.randint(10, 50)
            health -= random.randint(5, 15)
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

    if miles_traveled >= distance_to_oregon:
        print("Congratulations! You've reached Oregon successfully.")
    else:
        print("Game over. Your journey has ended.")


# Start the game
oregon_trail_game()
