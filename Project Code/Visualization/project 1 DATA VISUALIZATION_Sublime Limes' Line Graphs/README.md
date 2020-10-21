DATA VISUALIZATION
Sublime Limes' Line Graphs
In this project, you will be acting as a data analyst for an online lime retailer called Sublime Limes. People all over the world can use this product to get the freshest, best-quality limes delivered to their door. One of the product managers at Sublime Limes would like to gain insight into the customers and their sales habits. Using Matplotlib, you’ll create some different line graphs (or maybe, lime graphs) to communicate this information effectively.

If you get stuck during this project or would like to see an experienced developer work through it, click “Get Help“ to see a project walkthrough video.



Understand the data and set up subplots
1.
Add import codecademylib to the top of script.py. This will allow for your plots to render in our browser.

2.
We have provided some data in different lists in script.py. Look through these lists and try to understand what each one represents.

3.
Create a figure of width 12 and height 8.


4.
We are going to make two charts in one figure, laid out side-by-side. In other words, the figure will have one row and two columns, like this:

subplots

Write the command to create the left subplot (the one that would correspond to the plot with a star in our example figure). Save this subplot in a variable called ax1.


5.
Write the command to create the right subplot (the one that would correspond to the plot with a square in our example figure).

Save this subplot in a variable called ax2.

Page visits over time
6.
In the left subplot, we are going to plot the total page visits over the past year as a line.

First, let’s create the list of x-values, which is range(len(months)). Store this in a variable called x_values.

Make sure this happens after the line where you created ax1, but before the line where you’ve created ax2, so that the plot goes in the subplot on the left.

7.
Plot the total page visits against these x_values as a line.

8.
Give the line markers that will help show each month as a distinct value.

9.
Label the x-axis and y-axis with descriptive titles of what they measure.


10.
Set the x-axis ticks to be the x_values.

11.
Label the x-axis tick labels to be the names stored in the months list.

Plotting multiple lime species
12.
In the subplot on the right, we are going to plot three lines on the same set of axes. The x-values for all three lines will correspond to the months, so we can use the list of x_values we used for the last plot.

On one plot, create the three lines:

number of key limes sold vs x_values
number of Persian limes sold vs x_values
number of blood limes sold vs x_values
Make sure this happens after the line where you created ax2, so that it goes in the subplot on the right.

13.
Give each line a specific color of your choosing.

14.
Add a legend to differentiate the lines, labeling each lime species.

15.
Set the x-axis ticks to be the x_values, and the tick labels to be the months list.

Labeling and saving
16.
Add a title to each of the two plots you’ve created, and adjust the margins to make the text you’ve added look better.

17.
Now, save your figure as a png with a descriptive file name.
