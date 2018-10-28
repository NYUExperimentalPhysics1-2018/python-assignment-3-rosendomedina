#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
test tankshot and drawboard from tanks.py
requires completion of both of these items

@author: gershow

"""

from tanks import tankShot
from tanks import drawBoard
import matplotlib.pyplot as plt

tank1box = [100,150,0,50]
tank2box = [900,950,0,50]
obstacleBox = [400,600,0,500]


plt.figure(1)
drawBoard(tank1box,tank2box,obstacleBox,1)
hit = tankShot(tank2box, obstacleBox, 125,25,100,70)
plt.title ('a shot that goes over the target')
if hit:
    print ('you incorrectly detected a hit')

plt.figure(2)
drawBoard(tank1box,tank2box,obstacleBox,1)
hit = tankShot(tank2box, obstacleBox, 125,25,100,60)
plt.title ('a shot that hits the obstacle')
if hit:
    print ('you incorrectly detected a hit')

plt.figure(3)
drawBoard(tank1box,tank2box,obstacleBox,1)
hit = tankShot(tank2box, obstacleBox, 125,25,100,75)
plt.title ('a high arcing kill shot!')
if hit == 1:
    print ('you correctly detected a hit')
else:
    print ('you incorrectly reported a miss')
