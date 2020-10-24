MACHINE LEARNING: SUPERVISED LEARNING 🤖
Honey Production
Now that you have learned how linear regression works, let’s try it on an example of real-world data.

As you may have already heard, the honeybees are in a precarious state right now. You may have seen articles about the decline of the honeybee population for various reasons. You want to investigate this decline and how the trends of the past predict the future for the honeybees.

Note: All the tasks can be completed using Pandas or NumPy. Pick whichever one you prefer.

If you get stuck during this project or would like to see an experienced developer work through it, click “Get Help“ to see a project walkthrough video.



Check out the Data
1.
We have loaded in a DataFrame for you about honey production in the United States from Kaggle. It is called df and has the following columns:

state
numcol
yieldpercol
totalprod
stocks
priceperlb
prodvalue
year
Use .head() to get a sense of how this DataFrame is structured.


2.
For now, we care about the total production of honey per year. Use the .groupby() method provided by pandas to get the mean of totalprod per year.

Store this in a variable called prod_per_year.


3.
Create a variable called X that is the column of years in this prod_per_year DataFrame.

After creating X, we will need to reshape it to get it into the right format, using this command:

X = X.values.reshape(-1, 1)

4.
Create a variable called y that is the totalprod column in the prod_per_year dataset.


5.
Using plt.scatter(), plot y vs X as a scatterplot.

Display the plot using plt.show().

Can you see a vaguely linear relationship between these variables?


Create and Fit a Linear Regression Model
6.
Create a linear regression model from scikit-learn and call it regr.

Use the LinearRegression() constructor from the linear_model module to do this.


7.
Fit the model to the data by using .fit(). You can feed X into your regr model by passing it in as a parameter of .fit().

8.
After you have fit the model, print out the slope of the line (stored in a list called regr.coef_) and the intercept of the line (regr.intercept_).

9.
Create a list called y_predict that is the predictions your regr model would make on the X data.


10.
Plot y_predict vs X as a line, on top of your scatterplot using plt.plot().

Make sure to call plt.show() after plotting the line.


Predict the Honey Decline
11.
So, it looks like the production of honey has been in decline, according to this linear model. Let’s predict what the year 2050 may look like in terms of honey production.

Our known dataset stops at the year 2013, so let’s create a NumPy array called X_future that is the range from 2013 to 2050. The code below makes a NumPy array with the numbers 1 through 10

nums = np.array(range(1, 11))
After creating that array, we need to reshape it for scikit-learn.

X_future = X_future.reshape(-1, 1)
You can think of reshape() as rotating this array. Rather than one big row of numbers, X_future is now a big column of numbers — there’s one number in each row.

reshape() is a little tricky! It might help to print out X_future before and after reshaping.


12.
Create a list called future_predict that is the y-values that your regr model would predict for the values of X_future.


13.
Plot future_predict vs X_future on a different plot.

How much honey will be produced in the year 2050, according to this?
