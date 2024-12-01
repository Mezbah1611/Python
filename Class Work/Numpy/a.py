import numpy as np

Score = np.array([85,90,78,92,88])

# convert data type into float
Score = Score.astype(float)
print("Scores as float : ",Score)

#  scored as a_score 
a_score = Score.copy()
a_score += 5
print("Original Score",Score)
print("Modified Score : ",a_score)

# Find Shape ndim size itemsize dtype sort

print("Shape of Score : ",Score.shape)
print("Number of dimensions : ",Score.ndim)
print("size of array : ",Score.size)
print("Item size : ",Score.itemsize)
print("Item size  :",Score.dtype)
print("Datatype : ",Score.dtype)
print("Sorted Scores : ",np.sort(Score))

# d) Find the indices of scores greater than 80
indices = np.where(Score > 80)
print("Indices of scores > 80:", indices[0])

# e) Find min, max, std, var, sum, mean, axis-wise mean
print("Minimum score:", np.min(Score))
print("Maximum score:", np.max(Score))
print("Standard deviation:", np.std(Score))
print("Variance:", np.var(Score))
print("Sum of scores:", np.sum(Score))
print("Mean of scores:", np.mean(Score))

# f) Print scores using slicing
print("Every second score:", Score[::2])
print("Scores from index 1 to 4:", Score[1:4])
print("Last 3 scores in reverse order:", Score[-3::-1])