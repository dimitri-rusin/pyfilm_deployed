import numpy as np
import pyfilm as pf

x = np.random.rand(10)
y = np.random.rand(10)
z = np.random.rand(10, 10, 10)
pf.make_film_2d(x, y, z)
