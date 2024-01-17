# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 20:01:15 2024

@author: User
"""

import matplotlib.pyplot as plt

data = [
        [0,0,0,0,0,0,0,0],
        [0,0,1,1,1,1,0,0],
        [0,0,1,0,0,1,0,0],
        [0,0,1,0,0,1,0,0],
        [0,0,1,0,0,1,0,0],
        [0,0,1,0,0,1,0,0],
        [0,0,1,1,1,1,0,0],
        [0,0,0,0,0,0,0,0,]]

plt.imshow(data, cmap= 'gray')
plt.show()