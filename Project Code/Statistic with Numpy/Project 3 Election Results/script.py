import codecademylib
import numpy as np
import matplotlib.pyplot as plt

survey_responses = ['Ceballos', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos','Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 
'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 'Ceballos', 'Ceballos', 'Ceballos',
'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Ceballos',
'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Ceballos']

total_ceballos = sum([1 for i in survey_responses if i =='Ceballos'])

print('count ceballos '+str(total_ceballos))

percentage_ceballos = total_ceballos/float(len(survey_responses))
print('percentage ceballos '+ str(percentage_ceballos)) 

possible_surveys = np.random.binomial(float(len((survey_responses))),0.54,size=10000)/float(len(survey_responses))

# plt.hist(possible_surveys,bins=20,range=(0,1))
# plt.show()

ceballos_loss_surveys = np.mean(possible_surveys < 0.5)
print('loss percentage '+str (ceballos_loss_surveys))

large_survey = np.random.binomial(7000,0.5,size=10000)/7000
print('large_survey'+str(large_survey))
plt.hist(possible_surveys,bins=20,range=(0,1))
plt.hist(large_survey,alpha=.4,bins=20,range=(0,1))

plt.show()

ceballos_loss_new = np.mean(large_survey < 0.5)
print(ceballos_loss_new)
