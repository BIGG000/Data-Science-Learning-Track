LEARN STATISTICS WITH NUMPY
Election Results
You’re part of an impartial research group that conducts phone surveys prior to local elections. During this election season, the group conducted a survey to determine how many people would vote for Cynthia Ceballos vs. Justin Kerrigan in the mayoral election.

Now that the election has occurred, your group wants to compare the survey responses to the actual results.

Was your survey a good indicator? Let’s find out!

If you get stuck during this project or would like to see an experienced developer work through it, click “Get Help“ to see a project walkthrough video.



PROJECT STEPS
1.
First, import numpy and matplotlib.

2.
At the top of script.py is a list of the different survey responses.

Calculate the number of people who answered ‘Ceballos’ and save the answer to the variable total_ceballos.

Print the variable to the terminal to see its value.

3.
Calculate the percentage of people in the survey who voted for Ceballos and save it to the variable percentage_ceballos.

Print the variable to the terminal to see its value.




4.
In the real election, 54% of the 10,000 town population voted for Cynthia Ceballos. Your supervisors are concerned because this is a very different outcome than what the poll predicted. They want you to determine if there is something wrong with the poll or if given the sample size, it was an entirely reasonable result.

Generate a binomial distribution that takes the number of total survey responses, the actual success rate, and the size of the town’s population as its parameters. Then divide the distribution by the number of survey responses. Save your calculation to the variable possible_surveys.

5.
Plot a histogram of possible_surveys with a range of 0-1 and 20 bins.


6.
As we saw, 47% of people we surveyed said they would vote for Ceballos, but 54% of people voted for Ceballos in the actual election.

Calculate the percentage of surveys that could have an outcome of Ceballos receiving less than 50% of the vote and save it to the variable ceballos_loss_surveys.

Print the variable to the terminal.

7.
With this current poll, about 20% of the time a survey output would predict Kerrigan winning, even if Ceballos won the actual election.

Your co-worker points out that your poll would be more accurate if it had more responders.

Generate another binomial distribution, but this time, see what would happen if you had instead surveyed 7,000 people. Divide the distribution by the size of the survey and save your findings to large_survey.

8.
Now, recalculate the percentage of surveys that would have an outcome of Ceballos losing and save it to the variable ceballos_loss_new, and print the value to the terminal.

What do we notice about this new value?

What advice would you give to your supervisors about predicting results from surveys?
