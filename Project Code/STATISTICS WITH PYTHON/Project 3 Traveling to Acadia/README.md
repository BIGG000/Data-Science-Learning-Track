LEARN STATISTICS WITH PYTHON
Traveling to Acadia
Imagine you work at a travel agency and want to inform your customers of the best time to visit one of your favorite vacation locations, Acadia, Maine. In this project, you will use flower bloom data, and flight information to recommend the best time of year for someone to make a trip to Maine.

In script.py, we’ve imported the following data:

in_bloom is a NumPy array containing 900 numbers. Each number is a day of the year, which represents the average start date of a flower blooming.
flights is a NumPy array with 11,000 numbers. Each number is a day of the year, which represents a flight from your hometown to airports near Acadia, Maine.
Your goal is to create two histograms, each displaying the frequency of an occurrence each day of the year (either flights or flower blooms).

You will use the in_bloom variable to find a count of the number of flowers that start blooming each day of the year.

You will use the flights variable to find a count of the number of flights that occur each day of the year.





Making a Histogram
1.
Use Matplotlib to create a flights histogram.	
2.
If you haven’t done so already, set the range of your histogram to (0, 365)

3.
Set the number of bins in your plot to 365, so you have a separate bin for each day of the year

4.
Add an x-label, y-label, and title to your figure.


Multiple Plots
5.
Now, we’re going to set up our figure so it displays two plots at once. Above your plt.hist() line, add the following:

plt.figure(1)
plt.subplot(211)
6.
Between the last line for plotting your histogram and the show command, add plt.subplot(212).

At this point, your code should look something like:

plt.figure(1)
plt.subplot(211)

plt.hist(flights, range=(0, 365), bins=365)
plt.title("Flights by Day")
plt.xlabel("Day of the Year")
plt.ylabel("Flight Count")

plt.subplot(212)
# Next histogram below


plt.show()
Second Histogram
7.
Under plt.subplot(212), use plt.hist() to make a histogram that displays the number of flowers that begin to bloom each day of the year.

8.
Label the y-axis of the plot. In the hint, we’ve added our code.

Right before calling plt.show() call plt.tight_layout(). This will prevent the labels from overlapping with the graphs.

Thinking About the Data
9.
How would you use these histograms to help inform customers when they should go to Acadia, Maine. For example, if someone said they wanted to visit Acadia while there weren’t many people there, but while flowers were blooming, when would you recommend?

Check the hint to see how we answered this question.
