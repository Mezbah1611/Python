import numpy as np

def average_score(scores):
    average = np.mean(scores,axis= 1)

    average_index = np.argmax(average)
    high_avg_score = average[average_index]
    print(f"Student : {average_index + 1}, Highest Score : {high_avg_score}")

    return high_avg_score

scores = np.array([
    [85,90,78],
    [88,92,80],
    [90,91,95],
    [70,85,88]
])
average_score(scores)