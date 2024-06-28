# Portfolio Project 3 - Tic Tac Toe Game

Tic Tac Toe is a classic two-player game implemented in Python. The objective is to be the first to align three of your marks (X or O) in a row, column, or diagonal on a customizable n x n board. The game runs in a terminal and provides an interactive and engaging way for players to compete against each other or the computer. With clear instructions, robust input validation, and a replay option, this game offers a fun and challenging experience for all players.

![Screenshot from amiresponsivedesign](docs/imresponsive.png)

---

## Live Site

- [You can view the live site here](https://tic-tac-toe-miguel-ad5abe321650.herokuapp.com/)

## Github Repository

- [You can view the Github page here](https://github.com/MiguelMurilloG/tic_tac_toe.git)

---

## Site Goals

### Challenge and Reward:

- Provide a game that engages players with strategic challenges and rewards their efforts.

### Entertainment:

- Entertain users with interactive text-based gameplay in the terminal.

### Replayability:

- Encourage repeated play by offering a fun and addictive game experience.

---

## Existing Features

### Instructions

- Choose the size of the board (e.g., 3 for a 3x3 board).
- Players take turns entering their moves by specifying the row and column.
- The first player to get their marks in a row, column, or diagonal wins.
- If all cells are filled and no player has won, the game ends in a tie.

![Screenshot from heroku app](docs/instructions-game.png)

### Board Game
- After choosing to start a new game, the curremt state of the board is displayed

![Screenshot from heroku app](docs/board-game.png)

### Level Difficulty


### Win Message

- Player Wins: "Player X/O wins!"
- Tie Message: "It's a tie!"

![Screenshot from heroku app](docs/win-message.png)



---
## Possible Features

### Leaderboard:

- Track and display high scores or win counts for each player.
- Store player names and their win counts in a file or database.

### Multiple Game Modes:

- Add different game modes such as Classic, Timed, and Challenge modes.
- Timed mode could limit the amount of time a player has to make a move.

### AI Difficulty Levels:

- Implement multiple levels of AI difficulty: Easy, Medium, Hard.
- Adjust the computer's strategy based on the selected difficulty level.


---
## Bugs
- Corrected the input validation function structure.

![Screenshot from PEP8](docs/python-linter.png)


## Remaining Bugs
- No known bugs.

## Testing

### PEP8
- No errors were returned from (https://pep8ci.herokuapp.com)

---

## Deployment

The site was deployed to Heroku. Follow these steps to deploy the project:
- Create a new Heroku app.
- Name the app and select the appropriate region.
- Connect the GitHub repository to the Heroku app.
- In the app settings, add the buildpacks for Python and Node.js.
- Deploy the branch. Heroku will build and launch the game.

## Credits
- [Free Code Camp](https://www.freecodecamp.org): The foundational concepts and structure of this game were derived from this course.
- [W3Schools](https://www.w3schools.com):  Offered valuable resources and tutorials on Python
- [Slack Community](https://slack.com/intl/en-gb/): A helpful community for troubleshooting and solving coding challenges.

---

## Acknowledgements

I would like to express my deep appreciation to the following individuals and communities for their invaluable support and contributions throughout the development of the Tic Tac Toe game:

- Sheryl Goldberg: My mentor at Code Institute, whose constructive feedback and guidance were fundamental in shaping this project.
- Code Institute Tutor Team: Their continuous assistance and advice on coding challenges significantly contributed to the project's success.
- Code Institute Slack Community: The collaborative environment and shared expertise within the community were vital in overcoming development hurdles and maintaining motivation.