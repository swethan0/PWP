# -*- coding: utf-8 -*-
"""
Created on Mon Sep  1 13:43:26 2025

@author: reddy
"""

# Write a Python program to plot two or more lines on same plot with suitable legends of each line.

import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
y = [5, 4, 3, 2, 1]

plt.plot (x)
plt.plot (y)
plt.xlabel ("X-axis")
plt.ylabel ("Y-axis")
plt.title ("Line Graph")
plt.show ()