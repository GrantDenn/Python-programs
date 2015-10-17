import numpy as np
import matplotlib.pyplot as plt
num_points = 500
x_min, x_max = 0,4
x_values = np.linspace(x_min, x_max, num_points)
y_values = x_values**2
plt.plot(x_values, y_values)
plt.show()
