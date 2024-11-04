import numpy as np

Score = [85, 90, 78, 92, 88]

Score_array = np.array(Score, dtype=float)

a_Score = Score_array.copy()

a_Score += 5

print("After copying and modifying a_Score:")
print("a_Score:", a_Score)
print("Score_array:", Score_array)
print("  ")

a_Score = Score_array.view()

a_Score += 5

print("After viewing and modifying a_Score:")
print("a_Score:", a_Score)
print("Score_array:", Score_array)

print("\nProperties of Score_array:")
print("Shape:", Score_array.shape)
print("Number of dimensions (ndim):", Score_array.ndim)
print("Size (number of elements):", Score_array.size)
print("Item size (in bytes):", Score_array.itemsize)
print("Data type (dtype):", Score_array.dtype)

Score_sorted = np.sort(Score_array)
print("Sorted Score_array:", Score_sorted)


indices_above_80 = np.where(Score_array >= 80)
print("\nIndices of scores that are 80 or more:", indices_above_80[0])

max_value = np.max(Score_array)
min_value = np.min(Score_array)
std_deviation = np.std(Score_array)
variance = np.var(Score_array)
sum_value = np.sum(Score_array)
mean_value = np.mean(Score_array)

# Print statistics
print("\nStatistics:")
print("Max:", max_value)
print("Min:", min_value)
print("Standard Deviation:", std_deviation)
print("Variance:", variance)
print("Sum:", sum_value)
print("Mean:", mean_value)

Score_array_reshaped = Score_array.reshape(1, -1)


mean_axis_0 = np.mean(Score_array_reshaped, axis=0)
mean_axis_1 = np.mean(Score_array_reshaped, axis=1)

print("\nAxis-wise Mean:")
print("Mean along axis 0 (columns):", mean_axis_0)
print("Mean along axis 1 (rows):", mean_axis_1)


print("\nSlicing the Score list:")
print("Score[::2]:", Score[::2])
print("Score[-3:-1]:", Score[-3:-1])
print("Score[1:4]:", Score[1:4])
print("Score[2:4]:", Score[2:4])
print("Score[::4]:", Score[::4])
print("Score[::3]:", Score[::3])