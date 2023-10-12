"""
Name:Orgeon_trail_main

"""

#Import other files
#This will be were other members import their files for their rooms

#Define main
def main():

    #Print creative title (This will only print once, so it is before the loop)
    print("\nCreative title")
    print()

    #Set up loop
    #This loop is for the entire main program from start to finish. After that, we ask the user if they want to start over
    still_running = "y"
    while still_running == "y":
        
        #Main part of program
        main_game()

        #Ask user if they would like to play again
        still_running = input("Would you like to play again? [Y/N]: ").lower()

    #If user exits
    print("Thank you for playing!")

#This is the program that runs the game
def main_game():
    
    #The loop will always run up unless player health were to ever hit zero, then the loop breaks
    while True:

        #Create object
        game = Game()

        #----------------------------------------------------------------------


        #Arturo's stop
        game.health_lost = game.arturo_stop()

        #Subtract health from the amount of health lost during room
        game.subract_health()

        #Check health and end game if the player has no health
        check = game.check_health()

        if check == 0:
            game.game_over()
            break

        #----------------------------------------------------------------------
        
        #Aiden's stop
        game.health_lost =  game.aiden_stop()

        #Subtract health from the amount of health lost during room
        game.subract_health()

        #Check health and end game if the player has no health
        check = game.check_health()

        if check == 0:
            game.game_over()
            break

        #----------------------------------------------------------------------


        #Gus' stop
        game.health_lost = game.gus_stop()

        #Subtract health from the amount of health lost during room
        game.subract_health()

        #Check health and end game if the player has no health
        check = game.check_health()

        if check == 0:
            game.game_over()
            break

        #----------------------------------------------------------------------
        

        #Josiah's stop
        game.health_lost = game.josiah_stop()

        #Subtract health from the amount of health lost during room
        game.subract_health()

        #Check health and end game if the player has no health
        check = game.check_health()

        if check == 0:
            game.game_over()
            break

        #----------------------------------------------------------------------


        #Yonaton's stop
        game.health_lost = game.yonaton_stop()

        #Subtract health from the amount of health lost during room
        game.subract_health()

        #Check health and end game if the player has no health
        check = game.check_health()

        if check == 0:
            game.game_over()
            break
        
        #----------------------------------------------------------------------



        #If user reaches end, congrats
        print("You beat the game!")

        #End program funciton
        break






#Make object
class Game():

    #Initialize game health. This will be 100 at the beginning and will be lowered as player goes through rooms
    def __init__(self):


        self._health = 100
        self._health_lost = 0

    #If player health hits zero. We can later add cause of death later
    def game_over(self):
        print("You died!")

    #-------------------------------------------------ROOMS----------------------------------------------------
    #Each member will design their own rooms with their own challanges and what not. As of the current moment,
    #The only thing that will be returned is the amount of health lost during that room. Once the player goes
    #Through the room (Goes through the method), the program will check if the user's health is above 0 or not
    #If user health is not greater than 0, program ends.

    #TL:DR is to return the amount of health the player lost in the room
    #---------------------------------------------------------------------------------------------------------

    #Stop 1
    def arturo_stop(self):
        pass
        #Return the total amount of health lost during time in room





    #Stop 2
    def aiden_stop(self):
        pass
        #Return the total amount of health lost during time in room






    #Stop 3
    def gus_stop(self):
        pass
        #Return the total amount of health lost during time in room






    #Stop 4
    def josiah_stop(self):
        pass
        #Return the total amount of health lost during time in room






    #Stop 5 (End of game)
    def yonaton_stop(self):
        pass
        #Return the total amount of health lost during time in room








    #-----------------------------------------------------------------------------------------------------------------





    #---------------------------------------------------CALCULATIONS--------------------------------------------------
    #These will end up going into a different file since this file will just be for displaying.
    #Calculations like subtracting and checking health (later on, there might be more in here and could be a file
    # that is imported into other files to make calculations. For example, resting would add health and would be
    # another calculation)
    #-----------------------------------------------------------------------------------------------------------------

    def subract_health(self,):
        self._health = self._health - self._health_lost

        return self._health
    #Check current health
    def check_health(self):
        
        #If health is less than or equal to zero, end game
        if self._health <= 0:
            return 0
            
        #If health is greater than zero, print health and proceed
        print(f"Your health is at {self._health}")





#If alone, else module
if __name__ == "__main__":
    main()