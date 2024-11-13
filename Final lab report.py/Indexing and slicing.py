import numpy as np

sales_data = np.array([
    [100,200,450,550],
    [150,250,300,700],
    [500,200,450,400],
    [350,300,200,100]
    ])

print(sales_data)

print("\nSales data for first three product : ",sales_data[:3])

print("\nSales data for all procuts in last two month : ",sales_data[0:4,-2:])
print("\n Sales data for a specific product and month : ",sales_data[1,3])
