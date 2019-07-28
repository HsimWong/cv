import matplotlib.pyplot as plt
import numpy as np 
from scipy.signal import savgol_filter
mu, sigma = 0, 10

x = np.arange(1, 100, 0.1)  # x axis
z = np.random.normal(mu, sigma, len(x))
y = 100 + z[0:500]
y_ = 200 + z[500:570]
y__ = 100 + z[570:1000]
output = list(y) + list(y_) + list(y__)
w = savgol_filter(output, window_length=501, polyorder = 3)
plt.plot(x, w, linewidth=2, linestyle="-", c="b")  # it include some noise
plt.show()
