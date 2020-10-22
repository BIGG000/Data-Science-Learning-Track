VISUALIZATION CUMULATIVE PROJECTS
Twitch Part 1: Analyze Data with SQL
Twitch
Twitch is the world’s leading video platform and community for gamers, with 15%20 million unique daily visitors. Using data to understand its users and products is one of the chief responsibilities of the Twitch Science Team.

In this project, you will be working with two training tables that contain Twitch users’ stream (video) viewing data and chat room usage data.

Stream viewing data:

stream table
Chat usage data:

chat table
The Twitch Science Team provided this practice dataset. You can download the .csv files (800,000 rows) from GitHub.

Let’s get started!

If you get stuck during this project or would like to see an experienced developer work through it, click “Get Help“ to see a project walkthrough video.


Getting Started:
1.
Start by getting a feel for the stream table and the chat table:

Select all columns from the first 20 rows.

What columns do the tables have?

2.
What are the unique games in the stream table?

3.
What are the unique channels in the stream table?


Aggregate Functions:
4.
What are the most popular games in the stream table?

Create a list of games and their number of viewers using GROUP BY.


5.
These are some big numbers from the game League of Legends (also known as LoL).

Where are these LoL stream viewers located?

Create a list of countries and their number of LoL viewers using WHERE and GROUP BY


6.
The player column contains the source the user is using to view the stream (site, iphone, android, etc).

Create a list of players and their number of streamers.


7.
Create a new column named genre for each of the games.

Group the games into their genres: Multiplayer Online Battle Arena (MOBA), First Person Shooter (FPS), Survival, and Other.

Using CASE, your logic should be:

If League of Legends → MOBA
If Dota 2 → MOBA
If Heroes of the Strom → MOBA
If Counter-Strike: Global Offensive → FPS
If DayZ → Survival
If Survival Evolved → Survival
Else → Other
Use GROUP BY and ORDER BY to showcase only the unique game titles.

How does view count change in the course of a day?
8.
Before we get started, let’s run this query and take a look at the time column from the stream table:

SELECT time
FROM stream
LIMIT 10;
The data type of the time column is DATETIME. It is for storing a date/time value in the database.

Notice that the values are formatted like:

2015-01-01 18:33:52

So the format is:

YYYY-MM-DD HH:MM:SS


9.
SQLite comes with a strftime() function - a very powerful function that allows you to return a formatted date.

It takes two arguments:

strftime(format, column)

Let’s test this function out:

SELECT time,
   strftime('%S', time)
FROM stream
GROUP BY 1
LIMIT 20;
What do you think this does? Open the hint if you’d like to learn more.

10.
Okay, now we understand how strftime() works. Let’s write a query that returns three columns:

The hours of the time column
The view count for each hour
Lastly, filter the result with only the users in your country using a WHERE clause.


10.
Okay, now we understand how strftime() works. Let’s write a query that returns three columns:

The hours of the time column
The view count for each hour
Lastly, filter the result with only the users in your country using a WHERE clause.


12.
Good job! You have completed the SQL portion of the project. Before moving on to Part 2: Visualize data with Matplotlib, see what else you can dig up!

For example:

What are your favorite games? Can you find some insights about its viewers and chat room users?
Is there anything you can do after joining the two tables?
The full training .csv files are on GitHub.
