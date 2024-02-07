import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 50)
y = np.log(x)
plt.plot(x, y, "r")
plt.plot(y, x)
plt.show()