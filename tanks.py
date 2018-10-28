#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 19:18:02 2018

@author: gershow
"""
import numpy as np
import matplotlib.pyplot as plt

tank1Color = 'b'
tank2Color = 'r'
obstacleColor = 'k'

##### functions you need to implement #####
def trajectory (x0,y0,v,theta,g = 9.8, npts = 1000):
    """
    finds the x-y trajectory of a projectile
    
    parameters
    ----------
    x0 : float 
        initial x - position
    y0 : float
        initial y - position, must be >0
        initial velocity
    theta : float
        initial angle (in degrees)
    g : float (default 9.8)
        acceleration due to gravity
    npts : int
        number of points in the sample
    
    returns
    -------
    (x,y) : tuple of np.array of floats
        trajectory of the projectile vs time
    
    notes
    -----
    trajectory is sampled with npts time points between 0 and 
    the time when the y = 0 (regardless of y0)
    y(t) = y0 + vsin(theta) t - 0.5 g t^2
    0.5g t^2 - vsin(theta) t - y0 = 0
    t_final = v/g sin(theta) + sqrt((v/g)^2 sin^2(theta) + 2 y0/g)
    """
    vx = v * np.cos(np.deg2rad(theta))
    vy = v * np.sin(np.deg2rad(theta))
    tfinal = (vy/g) + np.sqrt((vy/g)**2 + 2*(y0)/g)
    t = np.linspace(0, tfinal, num = npts)
    x = x0 + vx*t
    y = y0 + vy*t - .5*g*(t**2)
    return x,y

def firstInBox (x,y,box):
    """
    finds first index of x,y inside box
    
    paramaters
    ----------
    x,y : np array type
        positions to check
    box : tuple
        (left,right,bottom,top)
    
    returns
    -------
    int
        the lowest j such that
        x[j] is in [left,right] and 
        y[j] is in [bottom,top]
        -1 if the line x,y does not go through the box
    """
    
    for j in x[0:len(x)]:
        if box[0] <= x[int(j)] <= box[1] and box[2] <= y[int(j)] <= box[3]:
            return int(j)
    return -1

        
def tankShot (targetBox, obstacleBox, x0, y0, v, theta, g = 9.8):
    """
    executes one tank shot
    
    parameters
    ----------
    targetBox : tuple
        (left,right,bottom,top) location of the target
    obstacleBox : tuple
        (left,right,bottom,top) location of the central obstacle
    x0,y0 :floats
        origin of the shot
    v : float
        velocity of the shot
    theta : float
        angle of the shot
    g : float 
        accel due to gravity (default 9.8)
    returns
    --------
    int
        code: 0 = miss, 1 = hit
        
    hit if trajectory intersects target box before intersecting
    obstacle box
    draws the truncated trajectory in current plot window
    """
    x, y = trajectory(x0, y0, v, theta, g=9.8, npts = 1000)
    x, y = endTrajectoryAtIntersection(x, y, obstacleBox)
    plt.plot(x, y, 'r')
    value = firstInBox(x, y, targetBox)
    if value >= 0:
        return 1
        print("hit")
    else:
        return 0
        print("Miss")
    showWindow()
    
def drawBoard (tank1box, tank2box, obstacleBox, playerNum):
    """
    draws the game board, pre-shot
    parameters
    ----------
    tank1box : tuple
        (left,right,bottom,top) location of player1's tank
    tank2box : tuple
        (left,right,bottom,top) location of player1's tank
    obstacleBox : tuple
        (left,right,bottom,top) location of the central obstacle
    playerNum : int
        1 or 2 -- who's turn it is to shoot
 
    """    
    plt.clf()
    drawBox(tank1box, 'b')
    drawBox(tank2box, 'r')
    drawBox(obstacleBox, 'k')
    plt.xlim(0,1000)
    plt.ylim(0,1000)
      
    showWindow() #this makes the figure window show up

def oneTurn (tank1box, tank2box, obstacleBox, playerNum, g = 9.8):   
    """
    parameters
    ----------
    tank1box : tuple
        (left,right,bottom,top) location of player1's tank
    tank2box : tuple
        (left,right,bottom,top) location of player1's tank
    obstacleBox : tuple
        (left,right,bottom,top) location of the central obstacle
    playerNum : int
        1 or 2 -- who's turn it is to shoot
     g : float 
        accel due to gravity (default 9.8)
    returns
    -------
    int
        code 0 = miss, 1 or 2 -- that player won
    
    clears figure
    draws tanks and obstacles as boxes
    prompts player for velocity and angle
    displays trajectory (shot originates from center of tank)
    returns 0 for miss, 1 or 2 for victory
    """        
    drawBoard(tank1box, tank2box, obstacleBox, playerNum)
    velocity = getNumberInput("Enter a Velocity> ")
    theta = getNumberInput("Enter an angle in degrees> ")
    if playerNum == 1:
        hitOrMiss = tankShot(tank2box, obstacleBox, 140, 40, int(velocity), int(theta), g=9.8)
        if hitOrMiss == 1:
            return playerNum
        else:
            return 0
    if playerNum == 2:
        hitOrMiss = tankShot(tank1box, obstacleBox, 910, 40, int(velocity), (int(theta) + 90), g=9.8)
        if hitOrMiss == 1:
            return playerNum
        else:
            return 0

def playGame(tank1box, tank2box, obstacleBox, g = 9.8):
    """
    parameters
    ----------
    tank1box : tuple
        (left,right,bottom,top) location of player1's tank
    tank2box : tuple
        (left,right,bottom,top) location of player1's tank
    obstacleBox : tuple
        (left,right,bottom,top) location of the central obstacle
    playerNum : int
        1 or 2 -- who's turn it is to shoot
     g : float 
        accel due to gravity (default 9.8)
    """
     
    playerNum = 1
    while True:
        end = oneTurn(tank1box, tank2box, obstacleBox, playerNum, g=9.8)
        if end == playerNum:
            break
        elif end == playerNum:
            break
        else:
            print("Miss")
            input("Hit enter to continue")
            if playerNum == 1:
                playerNum = playerNum + 1
            elif playerNum == 2:
                playerNum = playerNum - 1
    print("Hit, you won the game")
    print("Congratulations Player Number " + str(playerNum) + "!")
                     
##### functions provided to you #####
def getNumberInput (prompt, validRange = [-np.Inf, np.Inf]):
    """displays prompt and converts user input to a number
    
       in case of non-numeric input, re-prompts user for numeric input
       
       Parameters
       ----------
           prompt : str
               prompt displayed to user
           validRange : list, optional
               two element list of form [min, max]
               value entered must be in range [min, max] inclusive
        Returns
        -------
            float
                number entered by user
    """
    while True:
        try:
            num = float(input(prompt))
        except Exception:
            print ("Please enter a number")
        else:
            if (num >= validRange[0] and num <= validRange[1]):
                return num
            else:
                print ("Please enter a value in the range [", validRange[0], ",", validRange[1], ")") #Python 3 sytanx
            
    return num    

def showWindow():
    """
    shows the window -- call at end of drawBoard and tankShot
    """
    plt.draw()
    plt.pause(0.001)
    plt.show()


def drawBox(box, color):
    """
    draws a filled box in the current axis
    parameters
    ----------
    box : tuple
        (left,right,bottom,top) - extents of the box
    color : str
        color to fill the box with, e.g. 'b'
    """    
    x = (box[0], box[0], box[1], box[1])
    y = (box[2], box[3], box[3], box[2])
    ax = plt.gca()
    ax.fill(x,y, c = color)

def endTrajectoryAtIntersection (x,y,box):
    """
    portion of trajectory prior to first intersection with box
    
    paramaters
    ----------
    x,y : np array type
        position to check
    box : tuple
        (left,right,bottom,top)
    
    returns
    ----------
    (x,y) : tuple of np.array of floats
        equal to inputs if (x,y) does not intersect box
        otherwise returns the initial portion of the trajectory
        up until the point of intersection with the box
    """
    i = firstInBox(x,y,box)
    print(i)
    if (i < 0):
        return (x,y)
    return (x[0:i],y[0:i])


##### fmain -- edit box locations for new games #####
def main():
    tank1box = [100,150,0,50]
    tank2box = [900,950,0,50]
    obstacleBox = [400,600,0,500]
    playGame(tank1box, tank2box, obstacleBox, g=9.8)

def explanation():
    """
    I have looked over every single line of code in this program and every single line of the handout
    countless numbers of times and could not figure out the Issue.  To save you time and help you better 
    understand what is wrong with the code I will list the problems I had
    
    Biggest Problem: When I would run the code (this only started happening when I was almost done and had
    almost all of the lines written) the plot window would open up blank and not work i.e " Python is Not 
    Responding."  When I would close it the console would say, "Kernel died, restarting"
    
    firstInBox and endTrajectory would work with the obstacle, however firstInBox would not work with the
    targetBox i.e. identifying if the shot hit the other tank
    Note: In a desperate attempt to fix this, I mulitplied everything by a facter of 10, because my theory
    was that since j is almost always a float, and since you can only indice integers (among other things)
    and not floats, I hypothesized that j would skip a few key values in the x array that pertained to a 
    position where x was inbetween box[0] and box[1] since j would have to be an integer, and it could not take
    into account the floats in between where the shot could have registered
    
    When the shot would be too far (off of the right side of the screen in the case of player 1), the trajectory
    would not plot since the index would be out of bounds for the axis who's max value was at 1000, in my case.
    This would be an issue with firstInBox because j could not loop through the entire thing since sometimes
    the x[j] would be over 1000 and the axis is capped at 1000 (again, in my case it is 1000 since I desperately
    multiplied everything by 10, but the issue was still there even before when everything was at a normal scale,
    when the axis was 0-100)
    """

#don't edit the lines below;
if __name__== "__main__":
    main()  
        
    