import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer

# corpus = [
#     'This is the first document',
#     'This document is the second document',
#     'And this is the third one.',
#     'Is this the first document?'
# ]

corpus = [
    'Natural language processing is fun and interesting.',
    'I love learning about artificial intelligence and machine learning.',
    'Text analysis is a key component of data science.',
    'Machine learning and deep learning are important fields of AI.'
]

vectorizer = CountVectorizer()

X = vectorizer.fit_transform(corpus)

print("Fit transform is")

print("Features names: ", vectorizer.get_feature_names_out())
print(X.toarray())

df = pd.DataFrame(X.toarray(), columns=vectorizer.get_feature_names_out())

print("The generated DataFrame is:")
print(df)

# alldata = df[(df['this'] == 1) & (df['first'] == 1)]
# print("Indices where both 'this' and 'first' terms are present are", alldata.index.tolist())

alldata = df[(df['learning'] == 1) & (df['machine'] == 1)]
print("Indices where both 'learning' and 'machine' terms are present are", alldata.index.tolist())


# ordata = df[(df['this'] == 1) | (df['first'] == 1)]
# print("Indices where both 'this' and 'first' terms are present are", ordata.index.tolist())

ordata = df[(df['learning'] == 1) | (df['machine'] == 1)]
print("Indices where either 'learning' or 'machine' terms are present are", ordata.index.tolist())

# notdata = df[(df['and'] != 1)]
# print("Indices where 'and' term is not present", notdata.index.tolist())

notdata = df[(df['text'] != 1)]
print("Indices where 'text' term is not present", notdata.index.tolist())