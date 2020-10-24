import codecademylib3_seaborn
import matplotlib.pyplot as plt
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from svm_visualization import draw_boundary
from players import aaron_judge, jose_altuve, david_ortiz

fig, ax = plt.subplots()


aaron_judge.type = aaron_judge.type.map({'S':1,'B':0})
# print(aaron_judge.plate_x,aaron_judge.plate_z)

aaron_judge = aaron_judge.dropna(subset = ['type','plate_x','plate_z'])
# print(aaron_judge.plate_x.unique(),aaron_judge.plate_z.unique(),aaron_judge.type.unique())

plt.scatter(x = aaron_judge['plate_x'], y = aaron_judge.plate_z, c =aaron_judge.type, cmap = plt.cm.coolwarm, alpha = 0.25)

training_set,validation_set = train_test_split(aaron_judge,random_state=1)

largest = {'Value':0,'gamma':1,'C':1}
for gamma in range(1,4):
  for c in range(1,4):
    classifier =SVC(kernel='rbf',gamma=gamma,C=c)

    classifier.fit(training_set[['plate_x','plate_z']],training_set['type'])
    score = classifier.score(validation_set[['plate_x',
    'plate_z']],validation_set.type)

    if score > largest['Value']:
      largest['Value']=score
      largest['gamma']=gamma
      largest['C']=c
print(largest)

draw_boundary(ax,classifier)
plt.show()

