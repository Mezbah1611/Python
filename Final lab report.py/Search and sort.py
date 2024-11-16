import numpy as np

Scores = np.array([79,45,80,99,90,88,84])
search_score = [84,90]


for Score in search_score :
    indices = np.where(Score == Scores)[0]
    if indices>0:
        print('Indices : ',indices)
    else:
        print('Score Not found')


Ascending = np.sort(Scores)
print(Ascending)

Descending = np.sort(Scores)[::-1]
print(Descending)