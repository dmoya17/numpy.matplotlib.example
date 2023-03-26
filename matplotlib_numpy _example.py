# -*- coding: utf-8 -*-
"""
Learning Python
"""
# Implementation of matplotlib function
import numpy as np
np.random.seed(20000000)
import matplotlib.pyplot as plt
   
   
fig, ax = plt.subplots()
for color in [ 'tab:orange', 'tab:blue', 'tab:red']:
    n = 50
    x, y = np.random.rand(2, n)
    scale = 1000.0 * np.random.rand(n)
    ax.scatter(x, y, c = color, s = scale, label = color,
               alpha = 0.5)
   
fig.legend()
ax.grid(True)
  
fig.suptitle("""matplotlib.Figure.legend.EXAMPLE
SECOND LINE\n\n""", fontweight ="bold") 
    
plt.show() 
