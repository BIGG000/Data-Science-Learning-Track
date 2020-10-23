LEARN WEB SCRAPING WITH BEAUTIFUL SOUP
Chocolate Scraping with Beautiful Soup
After eating chocolate bars your whole life, you’ve decided to go on a quest to find the greatest chocolate bar in the world.

You’ve found a website that has over 1700 reviews of chocolate bars from all around the world. It’s displayed in the web browser on this page.

The data is displayed in a table, instead of in a csv or json. Thankfully, we have the power of BeautifulSoup that will help us transform this webpage into a DataFrame that we can manipulate and analyze.

The rating scale is from 1-5, as described in this review guide. A 1 is “unpleasant” chocolate, while a 5 is a bar that transcends “beyond the ordinary limits”.

Some questions we thought about when we found this dataset were: Where are the best cocoa beans grown? Which countries produce the highest-rated bars? What’s the relationship between cocoa solids percentage and rating?

Can we find a way to answer these questions, or uncover more questions, using BeautifulSoup and Pandas?




Make Some Chocolate Soup
1.
Explore the webpage displayed in the browser. What elements could be useful to scrape here? Which elements do we not want to scrape?


2.
Let’s make a request to this site to get the raw HTML, which we can later turn into a BeautifulSoup object.

The URL is:

https://content.codecademy.com/courses/beautifulsoup/cacao/index.html
You can pass this into the .get() method of the requests module to get the HTML.


3.
Create a BeautifulSoup object called soup to traverse this HTML.

Use "html.parser" as the parser, and the content of the response you got from your request as the document.

4.
If you want, print out the soup object to explore the HTML.

So many table rows! You’re probably very relieved that we don’t have to scrape this information by hand.

How are ratings distributed?
5.
How many terrible chocolate bars are out there? And how many earned a perfect 5? Let’s make a histogram of this data.

The first thing to do is to put all of the ratings into a list.

Use a command on the soup object to get all of the tags that contain the ratings.

6.
Create an empty list called ratings to store all the ratings in.

7.
Loop through the ratings tags and get the text contained in each one. Add it to the ratings list.

As you do this, convert the rating to a float, so that the ratings list will be numerical. This should help with calculations later.


8.
Using Matplotlib, create a histogram of the ratings values:

plt.hist(ratings)
Remember to show the plot using plt.show()!

Your plot will show up at localhost in the web browser. You will have to navigate away from the cacao ratings webpage to see it.

Which chocolatier makes the best chocolate?
9.
We want to now find the 10 most highly rated chocolatiers. One way to do this is to make a DataFrame that has the chocolate companies in one column, and the ratings in another. Then, we can do a groupby to find the ones with the highest average rating.

First, let’s find all the tags on the webpage that contain the company names.


10.
Just like we did with ratings, we now want to make an empty list to hold company names.

11.
Loop through the tags containing company names, and add the text from each tag to the list you just created.


12.
Create a DataFrame with a column “Company” corresponding to your companies list, and a column “Ratings” corresponding to your ratings list.

13.
Use .groupby to group your DataFrame by Company and take the average of the grouped ratings.

Then, use the .nlargest command to get the 10 highest rated chocolate companies. Print them out.

Look at the hint if you get stuck on this step!


Is more cacao better?
14.
We want to see if the chocolate experts tend to rate chocolate bars with higher levels of cacao to be better than those with lower levels of cacao.

It looks like the cocoa percentages are in the table under the Cocoa Percent column.

Using the same methods you used in the last couple of tasks, create a list that contains all of the cocoa percentages. Store each percent as an integer, after stripping off the % character.

15.
Add the cocoa percentages as a column called "CocoaPercentage" in the DataFrame that has companies and ratings in it.


16.
Make a scatterplot of ratings (your_df.Rating) vs percentage of cocoa (your_df.CocoaPercentage).

You can do this in Matplotlib with these commands:

plt.scatter(df.CocoaPercentage, df.Rating)
plt.show()
Call plt.clf() to clear the figure between showing your histogram and this scatterplot.

Remember that your plots will show up at the address localhost in the web browser.

17.
Is there any correlation here? We can use some numpy commands to draw a line of best-fit over the scatterplot.

Copy this code and paste it after you create the scatterplot, but before you call .show():

z = np.polyfit(df.CocoaPercentage, df.Rating, 1)
line_function = np.poly1d(z)
plt.plot(df.CocoaPercentage, line_function(df.CocoaPercentage), "r--")
Explore!
18.
We have explored a couple of the questions about chocolate that inspired us when we looked at this chocolate table.

What other kinds of questions can you answer here? Try to use a combination of BeautifulSoup and Pandas to explore some more.

For inspiration: Where are the best cocoa beans grown? Which countries produce the highest-rated bars?
