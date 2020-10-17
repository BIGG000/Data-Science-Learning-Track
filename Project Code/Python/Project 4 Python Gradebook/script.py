last_semester_gradebook = [("politics", 80), ("latin", 96), ("dance", 97), ("architecture", 65)]

subjects = ['physics', 'calculas', 'poetry', 'history']
grades = [98, 97, 85, 88]
subjects.append('computer Science')
grades.append(100)

gradebook = list(zip(subjects, grades))
gradebook.append(('Visual arts',93))


full_gradebook = gradebook + last_semester_gradebook
print (full_gradebook)

