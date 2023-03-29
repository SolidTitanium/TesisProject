import numpy as np
import matplotlib.pyplot as plt

a = np.arange(1, 25).reshape(2, 12)
a = np.hsplit(a, (2, 2))
print(a)

a = np.array([[0.45053314, 0.17296777, 0.34376245, 0.5510652],
              [0.54627315, 0.05093587, 0.40067661, 0.55645993],
              [0.12697628, 0.82485143, 0.26590556, 0.56917101]])

x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x)

# plt.plot(y, x)

fig, ax = plt.subplot_mosaic([["left", "right-top"],
                              ["left", "right-bottom"]])
ax["left"].plot(y, x)

plt.show()