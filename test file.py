import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

x_values = ['red', 'orange', 'yellow']
y_values = [5, 4, 6]

plt.bar(x_values, y_values, color = 'red')
plt.title('Sample Plot')
plt.xlabel('Xs')
plt.ylabel('Ys')
plt.show()