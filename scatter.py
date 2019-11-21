import matplotlib.pyplot as plt
import numpy as np

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [5, 12, 17, 23, 40, 35, 27, 45, 48, 50]

plt.scatter(x, y, label='graph', color='k')

plt.xlabel('x')
plt.ylabel('y')
plt.title('This is a scatter plot.')
plt.legend()
plt.show()