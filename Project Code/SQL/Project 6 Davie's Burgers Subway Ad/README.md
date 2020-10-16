Davie's Burgers Subway Ad
Davie's Burgers: The Sequel

Do you remember Davie’s Burgers from our Learn CSS course? Well, the restaurant business has been booming and it is now looking to place a catchy advertisement in the local subway station.

Help them dig into their orders table to see if there is anything interesting in there for a funny tagline!

If you get stuck during this project or would like to see an experienced developer work through it, click “Get Help“ to see a project walkthrough video.

1.
Start by getting a feel for the orders table:

SELECT *
FROM orders
LIMIT 10;
What are the column names?

2.
How recent is this data?

Use DISTINCT to find out all the unique order_date values in this table.

3.
The special_instructions column stores the data where Davie’s Burgers customers leave a note for the kitchen or the delivery.

Instead of selecting all the columns using *, write a query that selects only the special_instructions column.

Limit the result to 20 rows.

4.
There seem to be a lot of empty values in that column. That is because customers sometimes leave the notes section blank.

Can you edit the query so that we are only returning the special instructions that are not empty?

5.
Let’s go even further and sort the instructions in alphabetical order (A-Z).

6.
Awesome! Now we have a good idea of the list.

Let’s search for special instructions that have the word ‘sauce’.

Are there any funny or interesting ones?

7.
Let’s search for special instructions that have the word ‘door’.

Any funny or interesting ones?

8.
Let’s search for special instructions that have the word ‘box’.

Any funny or interesting ones?

9.
Wow, some of these are marketing gold! But what are their order numbers?

Instead of just returning the special instructions, also return their order ids.

For more readability:

Rename id as ‘#’
Rename special_instructions as ‘Notes’

10.
Great work! You have found special instructions that are funny and ridiculous - the perfect combo for a Davie’s Burgers tagline.

The marketing agency took it from there and worked out a subway ad in no time!
