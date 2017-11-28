import numpy as np

res = []
summert = []

for x in np.arange(1, 27, 0.5):
     for y in np.arange(1, 27, 0.5):
          for z in np.arange(1, 27, 0.5):
               if x*y*z == 27:
                    res.append([x, y, z])
               else:
                    pass

for i in range(len(res)):
     summert.append(sum(res[i]))

ind = summert.index(min(summert))

print(summert[ind])
print(res[ind])