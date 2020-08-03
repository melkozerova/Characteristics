import numpy as np
import math
import matplotlib.pyplot as plt

x1 = np.linspace(-100, 100, 10000)
t1 = np.linspace(-100, 100, 10000)

x2 = np.linspace(-100, 100, 10000)
t2 = np.linspace(-100, 100, 10000)

c = [0]*100
d = [-1]*100

f, axs = plt.subplots(2, 2, figsize=(14, 7))
f.suptitle('Characteristics plot')
plt.subplot(1, 1, 1)
plt.xlim(0, 1)
plt.ylim(0, 10)
plt.title('First family and second family')
plt.xlabel('x')
plt.ylabel('t')

for x0 in range(0, 100):
    t1 = (x1 - 0.1*x0) / (4/math.pi * math.atan(0.1*x0 - 2) + 2)
    plt.plot(x1, t1, color = 'red', linewidth = 0.5)

#plt.subplot(1, 2, 2)
#plt.title('Second family')
#plt.xlim(0, 2)
#plt.ylim(0, 10)

for t0 in range(0, 100):
    x2 = (2 - 4/math.pi * math.atan(2)) * math.exp(-0.1*t0) * (t2 - 0.1*t0)
    plt.plot(x2, t2, color = 'blue', linewidth = 0.5)



#plt.subplot(1, 1, 1)
plt.show()