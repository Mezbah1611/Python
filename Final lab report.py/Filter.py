import numpy as np

prices = np.array([20,40,70,45,90,96,48,10,35])

minmum_price = 20
maximum_price = 60

filter_Price = [(prices >=minmum_price) & (prices<=maximum_price)]
print('Prices Between the range : ',filter_Price)