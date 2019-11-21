import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("Pokemon.csv")
g1 = data.plot.scatter(x='Defense', y='Attack', c=data['Speed'],
                       colormap='Spectral',title='ATK vs DEF over SPD')

"""df = pd.DataFrame([[5.1, 3.5, 0], [4.9, 3.0, 0], [7.0, 3.2, 1],
                  [6.4, 3.2, 1], [5.9, 3.0, 2]],
                  columns=['length', 'width', 'species'])
ax1 = df.plot.scatter(x='length', y='width', c='DarkBlue')"""