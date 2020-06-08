import matplotlib.pyplot as plt
import numpy as np
from scipy import interpolate



fig, (ax1, ax2) = plt.subplots(1, 2)
plt.subplots_adjust(hspace=0.4,wspace=0.4)
x=[0.0, 0.0, 0.01, 0.05, 0.1, 0.15, 0.19, 0.3, 1.0]
y=[0.0, 0.8, 0.81, 0.85, 0.9, 0.95, 0.99, 1.0, 1.0]

f = interpolate.interp1d(x, y, kind="linear")
x_int = np.linspace(x[0],x[-1], 2)
y_int = f(x_int)

ax1.plot([0.0, 0.0, 0.01, 0.05, 0.1, 0.15, 0.19, 0.3, 1.0], [0.0, 0.8, 0.81, 0.85, 0.9, 0.95, 0.99, 1.0, 1.0], 'm')
ax1.plot([0.0, 1.0], [0.0, 1.0], 'k--')
ax1.set_xlabel("true positive rate")
ax1.set_ylabel("False Positive rate")
ax1.set_title("Train AUC 0.83...")

x2=[0.0, 0.05, 0.1, 0.2, 0.30, 0.38, 0.4, 0.6, 0.7,0.85, 1.0]
y2=[0.0, 0.0, 0.1, 0.18, 0.2, 0.4, 0.5, 0.55, 0.6,0.9,1.0]
f2 = interpolate.interp1d(x2, y2, kind ='linear')

for i in [2,10,20,30,40,50]:
    x2_int=np.linspace(x2[0],x2[-1], i)
    y2_int = f2(x2_int)
    ax2.plot(x2_int, y2_int, 'm',)
    ax2.plot([0.0, 1.0], [0.0, 1.0], 'k--')

ax2.set_xlabel("true positive rate")
ax2.set_ylabel("False Positive rate")
ax2.set_title("Test AUC ...")


fig.show()