# -------------------------------------------------------------------------
#
# PYTHON for DUMMIES 18-19
# Problème 3
#
# Script de test un peu plus rigolo
# Pour introduite un point : faire un clic sur la figure
# Un double clic permet d'obtenir le calcul de la courbe d'Hermite
#
#  Vincent Legat
#
# -------------------------------------------------------------------------
# 

import matplotlib
from matplotlib import pyplot as plt
from numpy import *
from spline import spline

# ====================== callback pour les événements avec la souris ======
#
#  Observer la gestion distincte du clic simple et double :-)
#  Apres un evenement, on redessine la figure avec draw()
#

def mouse(event):
  global X,Y,n
  if (event.dblclick):
    t  = arange(0,n+0.001,0.001)
    x  = spline(t,1.0,X)
    y  = spline(t,1.0,Y)
    plt.plot(x,y,'-b')
    X,Y = [],[]; n = 0
  else :    
    x = event.xdata 
    y = event.ydata
    if (x != None and y != None) :
      n = n + 1
      X = append(X,[x])
      Y = append(Y,[y])
      print("New data : " + str(x) + "," + str(y))
      plt.plot([x],[y],'.r',markersize=10)
  fig.canvas.draw()


# ============================= mainProgram ===============================
 
matplotlib.rcParams['toolbar'] = 'None'
matplotlib.rcParams['lines.linewidth'] = 1
plt.rcParams['figure.facecolor'] = 'silver'

X,Y = [],[]; n = 0   
fig = plt.figure("Cubic spline interpolation")
fig.canvas.mpl_connect('button_press_event',mouse)
plt.ylim((0,1)); plt.xlim((0,1.3)); plt.axis("off")

plt.show()



