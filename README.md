# La Aventura del Sendero de Oregon (The Oregon Trail Adventure)

- [La Aventura del Sendero de Oregon (The Oregon Trail Adventure)](#la-aventura-del-sendero-de-oregon-the-oregon-trail-adventure)
  - [Collaborators](#collaborators)
  - [Story](#story)
  - [Stops Along The Way](#stops-along-the-way)
- [Coding the Adventure](#coding-the-adventure)
  - [Project Status Videos](#project-status-videos)
  - [Expand the Game Ideas](#expand-the-game-ideas)
    - [License](#license)

![](/img/welcome_to_game.png)

Play the game on Replit: [Oregon Trail Adventure](https://replit.com/@itinstructor/OregonTrailAdventure)

A shared coding adventure for Intro to Computer Science Fa23.

## Collaborators
1. Aidan Newberry (regtoga)
2. Arturo Montiel (Montiel8)
3. Yonatan Getachew (Yogetachew)
4. Josiah Andrews (siahdrews)
5. Braxton Rider (SirRexOfRider)
6. Gus Allred (itsjustmegus)
7. Jesse Bunnell (xGhostProjectx)

## Story

Everything You Wanted to Know about the [Oregon Trail Game](https://www.died-of-dysentery.com/index.html)

[Overview of the Oregon Trail Game](https://www.died-of-dysentery.com/oregon-trail.html)

"The Oregon Trail Adventure" is a text-based, strategy-driven game where you, as a pioneer, embark on a perilous journey along the historic Oregon Trail in the year 1848. Your choices will determine the fate of your party as you face challenges such as river crossings, mountain passes, and resource management. Navigate wisely to reach the fertile lands of Oregon and fulfill your dreams of a new life in the American West.

To play "The Oregon Trail Adventure," follow these steps:

1. Start the game and enter your name to begin your journey as a pioneer.
2. Use the main menu to make choices:
   - "Travel to the next stop" to continue your journey.
   - "Check player status" to monitor your health, food, and money.
   - "Quit" to exit the game.
3. During your journey, you'll encounter various stops, each with its own challenges.
4. Make decisions at each stop, such as fording rivers or searching for resources.
5. Manage your resources wisely, including food and money, to ensure your party's survival.
6. Progress on the trail, and your choices will shape the outcome of your adventure.
7. Your goal is to reach the Willamette Valley in Oregon, so plan your moves carefully.
8. Navigate the trail successfully to achieve your dreams in the American West.

Remember, keep an eye on your health, make good choices, and travel successfully to Oregon City. Good luck!

## Stops Along The Way

- Independence, Missouri
- Kansas River Crossing
- Big Blue River Crossing
- Fort Kearney
- Chimney Rock
- Fort Laramie
- Independence Rock
- South Pass
- Green River Crossing
- Fort Bridger
- Soda Springs
- Fort Hall
- Snake River Crossing
- Fort Boise
- Blue Mountains
- Fort Walla Walla
- The Dalles
- Willamette Valley, Oregon

[More about the stops along the way](https://www.philipbouchard.com/oregon-trail/real-geography.html)

# Coding the Adventure

We are crating a text-based "Oregon Trail" game in Python with a command-line interface. In this game, travelers will make choices as they embark on their journey. Here's an overview of how the program works and how to contribute to it.

1. **Fetch** the current copy of the code from GitHub. You don't want to overwrite someone else's work.
1. The main folder has the following files.
   - `main.py` (Game menu)
   - `player.py` (Player class)

2. Make a duplicate of the stop.py file in the stops folder. Rename it to your stop. We are following the Oregon trail stops as shown below.
3. Rename your stop to match one of the stops
   - `start.py` (Starting location: Independence, Missouri)
   - `kansas_river.py` (Kansas River Crossing)
   - `big_blue_river.py` (Big Blue River Crossing)
   - `fort_kearney.py` (Fort Kearney, NE)
   - `chimney_rock.py` (Chimney Rock, NE)
   - `fort_laramie.py` (Fort Laramie, WY)
   - `independence_rock.py` (Independence Rock, WY)
   - `south_pass.py` (South Pass, WY)
   - `green_river_crossing.py` (Green River Crossing)
   - `fort_bridger` (Fort Bridger)
   - `soda_springs`(Soda Springs)
   - Fort Hall
   - Snake River Crossing
   - Fort Boise
   - Blue Mountains
   - Fort Walla Walla
   - The Dalles
   - `end.py` (Willamette Valley, Oregon)

4. In the main.py file --> Add your stop to the STOPS list in the following format.

```
# Define the stops along the Oregon Trail
STOPS = [
    KansasRiver("Kansas River Crossing"),
    NorthPlatteRiver("North Platte River")
]
```

5. Finish building your stop. Take a look at the current stops to get ideas on how to code your stop.
6. Once you've created all location classes and connected them through the game menu in `main.py`, players can navigate through the game by making choices and progressing through the locations.
7. Commit early, Commit often

You can expand and customize the game by adding more details, challenges, and interactions at each location. Make sure to handle game over conditions and keep track of the player's progress throughout the journey.

## Project Status Videos

- 11-02 [Video of project status and next steps](https://wnccnet-my.sharepoint.com/:v:/g/personal/loringw_wncc_edu/EaYm9UcJVFNFh6vahACxQR8B2vQDaizOkfBgDp9SWkdPiA?e=TBNC2D)

## Expand the Game Ideas

1. **Add More Stop Classes:**
   - Create additional stop classes, representing various real-life locations and events along the Oregon Trail. Examples include forts, trading posts, Native American encounters, and more. Each stop should have unique descriptions and interactions.

2. **Random Events:**
   - Implement random events that can occur during the journey, such as illness, theft, wildlife encounters, and natural disasters. Create decision points for players to handle these events.

3. **Inventory Items:**
   - Introduce a wider variety of inventory items, such as tools, clothing, medicine, and weapons. Allow players to find, trade, or purchase these items during their journey.

4. **Character Development:**
   - Give players the option to create a character profile at the beginning of the game, specifying their occupation, skills, and background. These choices could affect gameplay, such as hunting proficiency or trade negotiations.

5. **Dynamic Weather and Seasons:**
   - Implement dynamic weather conditions and seasons, affecting travel speed, food availability, and other gameplay elements. Players should adapt their strategies accordingly.

6. **Multiplayer and Trading:**
   - Develop a multiplayer feature that allows players to trade resources, form caravans with other players, or compete to reach the destination first.

7. **Quests and Objectives:**
   - Create optional quests and objectives that players can complete for rewards. These quests could involve helping other pioneers or solving mysteries along the trail.

8. **Resource Management:**
   - Expand the resource management aspect of the game. Introduce a more detailed economy, where prices fluctuate, and supplies become scarcer as the journey progresses.

9. **Educational Elements:**
   - Incorporate historical facts and educational content about the Oregon Trail and its significance in American history. This can make the game both entertaining and informative.

10. **Graphics and User Interface:**
    - Enhance the game with a graphical user interface (GUI) to provide a more immersive experience. Use images and visual cues to represent events, characters, and locations.

11. **Endings and Scenarios:**
    - Create multiple possible endings based on the player's decisions and achievements. Allow for different outcomes, ranging from success in Oregon to unfortunate circumstances along the trail.

12. **Community and Mods:**
    - Build a community around the game and allow modding to encourage players to create their own content, including new stops, events, and characters.

13. **Testing and Feedback:**
    - Regularly playtest the game and gather feedback from players to fine-tune gameplay, balance, and user experience.

By following these directions, you can expand "The Oregon Trail Adventure" into a more complex and engaging game with diverse gameplay elements and a rich historical context.

### License

<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a><br />

This work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License](http://creativecommons.org/licenses/by-nc-sa/4.0/)</a>.