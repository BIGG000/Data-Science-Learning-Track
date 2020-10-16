The Metropolitan Museum of Art
The Met
The Metropolitan Museum of Art of New York is one of the world’s largest and finest art museums.

In this project, you will be working with a table named met that contains the museum’s collection of American Decorative Arts.

It has the following columns:

id - the id of the art piece
department - the department of the art piece
category - the category of the art piece
title - the title name of the art piece
artist - the name of the artist
date - the date(s) of the art piece
medium - the medium of the art piece
country - the country of the artist
This data was kindly made publicly available under the Open Access Policy.

Let’s get started!

If you get stuck during this project or would like to see an experienced developer work through it, click “Get Help“ to see a project walkthrough video.


1.
Start by getting a feel for the met table:

SELECT *
FROM met
LIMIT 10;
What are the column names?


2.
How many pieces are in the American Decorative Art collection?


3.
Celery was considered a luxurious snack in the Victorian era (around the 1800s). Wealthy families served stalks of it in intricate glass vases.

Don’t believe it?

Count the number of pieces where the category includes ‘celery’.


4.
Find the title and medium of the oldest piece(s) in the collection.


5.
Not every American decoration is from the Americas… where are they are coming from?

Find the top 10 countries with the most pieces in the collection.


6.
There are all kinds of American decorative art in the Met’s collection.

Find the categories HAVING more than 100 pieces.

7.
Lastly, let’s look at some bling!

Count the number of pieces where the medium contains ‘gold’ or ‘silver’.

And sort in descending order.
