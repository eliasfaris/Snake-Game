# Snake-Game-Webapp-CMPE-131

https://travis-ci.org/akumar23/Snake-Game-Webapp-CMPE-31

Run the program by cloning the github, running 'pip install requirements.txt' (without the quotes) and executing rungame.py, then going to the link that it provides, which should be http://127.0.0.1:5000/.

The 8 features include:
Allowing users to register with a unique username, allowing them to login with their registered credintials and allow them to logout from every page.
Once they log in, they get sent to a color picker page that has links to different versions of the snake game with different colors for the body of the snake.
One of the options on the color pickers page lets users play a harder version of the game which places an extra dot on the screen that they have to avoid as they collect food.
When users die in the game, their final score is then saved into a leaderboard and they are automatically redirected to it upon death. The page can also be accessed from every page, but this feature is still being worked on.
In the middle or end of a game session the user can also press the button 'r' to restart the game.
Admins can also acess an adminpanel by going to http://127.0.0.1:5000/adminpanel, which will soon be protected by a password, and clear the database of all users in case of emergencies.
We also worked on css to make the site have a uniform design and look clean.
