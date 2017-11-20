# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

n = 10000
I = 9503
bkg = 207
sp = 25 * 10**(-3)
sm = 600 * 10**(-3)

Imars = np.array([6728, 7623, 5987])
l = np.array([3.1 * 10**(-2), 1.8 * 10**(-2), 4 * 10**(-2)])

mu = np.zeros(len(l))
d = np.zeros(len(l))
x = np.zeros(len(l))

xp = np.linspace(0.15, 0.5, n)
Ip = np.zeros(len(xp))

mu = np.log(Imars / (I-bkg)) / (-l)
d = np.log(2) / mu
x = np.log(sp / sm) / (-mu)

mua = sum(mu) / len(mu)
da = sum(d) / len(d)
xa = sum(x) / len(x)

Ip = I * np.exp(-mua * xp)

stp = sm * np.exp(-mua * xp)

print(mua, "My [m^-1]\n", da, "Halverditykkelse [m]\n", xa, "Distanse [m]")

bol = True

for i in range(len(xp)):
    if stp[i] <= sp and bol == True:
        print("\n", stp[i], "Stråling [Sv]\n", xp[i], "Distanse under bakken [m]")
        bol = False

plt.plot(xp, stp)
plt.xlabel("Distanse under bakken [m]")
plt.ylabel("Stråling [Sv]")
plt.show()