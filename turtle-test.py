from turtle import *
from random import random

for i in range(100):
    # color(float(random() *256), float(random() *256), float(random() * 256))
    steps = int(random() * 100)
    angle = int(random() * 360)
    right(angle)
    forward(steps)


mainloop()