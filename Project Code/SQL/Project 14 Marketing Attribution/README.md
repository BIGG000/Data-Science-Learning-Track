You Can Check Table over here
https://content.codecademy.com/courses/sql-intensive/page_visits_schema.pdf



ANALYZE REAL DATA WITH SQL
Attribution Queries
CoolTShirts sells shirts of all kinds, as long as they are T-shaped and cool. Recently, CTS started a few marketing campaigns to increase website visits and purchases. Using touch attribution, they’d like to map their customers’ journey: from initial visit to purchase. They can use that information to optimize their marketing campaigns. This project will guide you through some of that process.

At this point you should have taken the lesson on touch attribution. This project will guide you through a number of queries on CoolTShirts’ user data (see the schema here).

Check off the steps as you go. In the rare chance that your project gets stuck in a bad state — maybe you accidentally edited the data —, refresh the page.

If you get stuck during this project or would like to see an experienced developer work through it, click “Get Help“ to see a project walkthrough video.



Get familiar with CoolTShirts
1.
How many campaigns and sources does CoolTShirts use? Which source is used for each campaign?

Use three queries:

one for the number of distinct campaigns,
one for the number of distinct sources,
one to find how they are related.

2.
What pages are on the CoolTShirts website?

Find the distinct values of the page_name column.


What is the user journey?
3.
How many first touches is each campaign responsible for?

You’ll need to use the first-touch query from the lesson (also provided in the hint below). Group by campaign and count the number of first touches for each.


4.
How many last touches is each campaign responsible for?

Starting with the last-touch query from the lesson, group by campaign and count the number of last touches for each.


5.
How many visitors make a purchase?

Count the distinct users who visited the page named 4 - purchase.

6.
How many last touches on the purchase page is each campaign responsible for?

This query will look similar to your last-touch query, but with an additional WHERE clause.


7.
CoolTShirts can re-invest in 5 campaigns. Given your findings in the project, which should they pick and why?
