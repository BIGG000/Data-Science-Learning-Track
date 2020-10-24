from sklearn.datasets import fetch_20newsgroups
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer

emails = fetch_20newsgroups()
# print(emails.target_names)

train_emails = fetch_20newsgroups(categories = ['comp.sys.ibm.pc.hardware','rec.sport.hockey'],subset= 'train',shuffle=True,random_state = 100)
print(train_emails.data[5])
print(train_emails.target)
print(train_emails.target_names)

test_emails = fetch_20newsgroups(categories = ['comp.sys.ibm.pc.hardware','rec.sport.hockey'],subset= 'test',shuffle=True,random_state = 100)

counter = CountVectorizer()

counter.fit(test_emails.data + train_emails.data)

train_count = counter.transform(train_emails.data)
test_count = counter.transform(test_emails.data)

classifier = MultinomialNB()

classifier.fit(train_count,train_emails.target)

print(classifier.score(test_count,test_emails.target))







