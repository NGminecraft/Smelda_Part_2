"""
import numpy as np

c= []
with open("Legend of smelda - Big Collision.csv", "r") as csv:
    readCsv = csv.read()
    csv = readCsv.split("\n")
    for i in csv:
        c.append(i.split(","))

print(np.save("BigMapCollision", np.asarray(c)))
"""

import sys
print(sys.path)
print(type(sys.path))
a = sys.path
a = a[0].split("\\")
print(a)
del a[-1]
print("\\".join(a))