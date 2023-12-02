'''
*****************************************************************************************
*
*        		===============================================
*           	               e-Yantra mini assignment 1
*        		===============================================
*
*  This script is to be used to implement Mini Assignment titled- 'Drawing Polygons using Turtle'.
*  
*  This software is made available on an "AS IS WHERE IS BASIS".
*  Licensee/end user indemnifies and will keep e-Yantra indemnified from
*  any and all claim(s) that emanate from the use of the Software or 
*  breach of the terms of this agreement.
*  
*  e-Yantra - A MOE project under National Mission on Education using ICT (NMEICT)
*
*****************************************************************************************
'''

# Team ID:          
# 					[ Team-ID ]
# Author List:      
# 					[ Names of team members worked on this file separated by Comma: Name1, Name2, ... ]
# Filename:         bar_graph.py
# Functions:        
#                   [ Comma separated list of functions in this file ]
# Global variables: 
# 					[ List of global variables defined in this file ]


####################### IMPORT MODULES #######################
## You are not allowed to make any changes in this section. ##
## You have to implement this assignment with the available ##
## modules for this task.								    ##
##############################################################

import turtle
import random

ls_height = [138, 145, 164, 130, 157, 145, 169, 120]
ls_weight = [30, 49, 40, 35, 40, 45, 48, 38]

"""
Purpose:
---
Use the following lines of code to write the definition of the function to show the given data on the bar graph, return mean & median  .
---
"""

##############	ADD YOUR CODE HERE	##############

def turtle_movement(mm, angle):
    polygon.forward(mm)
    polygon.right(angle)

def draw_bargraph(ls):
    polygon.left(90)
    sum = 0
    for i in ls:
        sum += i
        polygon.begin_fill()
        turtle_movement(i,90)
        polygon.write(str(i), font= ('Arial', 8))
        turtle_movement(25,90)
        turtle_movement(i,-90)
        polygon.end_fill()
        polygon.forward(10)
        polygon.left(90)
        mean = sum/len(ls)
        median = ((ls[int(len(ls)/2)] + ls[int((len(ls)-1)/2)])/2) if (len(ls)%2 == 0) else ls[int(len(ls)/2)]
        string = "Mean = {:.2f},\n Median = {:.2f}".format(mean, median)
    polygon.write(string, font=('Arial', 12))



##################################################




"""
Purpose:
---
Use the following lines of code  to initialize the screen that is to be used by turtle 
	
NOTE: 
1. Width and Height of the screen should both be 800 pixels.
2. Team has to use data given by e-Yantra Team to plot the bar graph.
---
"""

##############	ADD YOUR CODE HERE	##############

scrn = turtle.Screen()
scrn.setup(800, 800)
scrn.title("e-Yantra School Robotics Competition")
polygon = turtle.Turtle()
polygon.fillcolor('green')
polygon.penup()
polygon.setpos(-200, 100)

##################################################


"""
Purpose:
---
Use the following lines of code  to call the function to show the student's height data on bar graph ,set position of the turtle to display the mean & median on the screen.
 
NOTE:
1. Team has to use data(student's height in form of list) given by e-Yantra Team to plot the bar graph.
"""

##############	ADD YOUR CODE HERE	##############

polygon.pendown()
draw_bargraph(ls_height)
polygon.penup()


##################################################





"""
Purpose:
---
Use the following lines of code  to call the function to show the student's weight data on bar graph ,set position of the turtle to display the mean & median on the screen.

NOTE:
1. Team has to use data(student's weight in form of list) given by e-Yantra Team to plot the bar graph.
"""

##############	ADD YOUR CODE HERE	##############
polygon.setpos(-200, -150)
polygon.right(90)
polygon.pendown()
draw_bargraph(ls_weight)
turtle.mainloop()
##################################################


