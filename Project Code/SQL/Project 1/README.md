THE IMPORTANCE OF DATA AND SQL BASICS
Create a Table
In this project, you will create your own friends table and add/delete data from it!

The instructions provided are a general guideline. Feel free to add more columns, insert more data, and create more tables.

1.
Create a table named friends with three columns:

id that stores INTEGER
name that stores TEXT
birthday that stores DATE

2.
Beneath your current code, add Jane Doe to friends.

Her birthday is May 30th, 1990.

3.
Let’s make sure that Jane has been added to the database:

SELECT * 
FROM friends;
Check for two things:

Is friends table created?
Is Jane Doe added to it?

4.
Let’s move on!

Add two of your friends to the table.

Insert an id, name, and birthday for each of them

5.
Jane Doe just got married! Her new last name is “Smith”.

Update her record in friends.

6.
Add a new column named email.

7.
Update the email address for everyone in your table.

Jane Smith’s email is jane@codecademy.com.

8.
Wait, Jane Smith is not a real person.

Remove her from friends.

9.
Great job! Let’s take a look at the result one last time:

SELECT * 
FROM friends;
