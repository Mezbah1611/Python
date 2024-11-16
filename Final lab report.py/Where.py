import numpy as np

tempeatures = np.array([17,12,15,18,19,20,30,40,42,22,38,44])

high = 40
low = 17

exceeds_temperature = np.where(tempeatures>high)[0]
print('Temperature Exceeds',exceeds_temperature)

adjusted_temperature = np.where(tempeatures<low,low,tempeatures)
print('Replaced : ',adjusted_temperature)