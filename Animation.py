from numpy import *
import matplotlib.pyplot as plt

plt.figure(figsize = (24, 20))
def graphPointTime(time):
    '''
    takes a time and graphs the vector along the transformation at that time
    '''
    global a
    global b
    global c
    global ta
    global tb
    global tc
    
    at = a + time * (ta - a)
    bt = b + time * (tb - b)
    ct = c + time * (tc - c)
    
    plt.plot([at[0], bt[0], ct[0], at[0]], [at[1], bt[1], ct[1], at[1]], 'ro-', color = (1-time, time, 0.1 +  0.5 * time))
    

#3 initial position vectors
a = array([2,2])
b = array([1, -2])
c = array([-2, -1])

#matrix to represent the transformation
t = array([[-3, 0], [0, 3]])

#calculating final transformed matrixes
ta = t.dot(a)
tb = t.dot(b)
tc = t.dot(c)




t = 0
while (t < 1):
    graphPointTime(t)
    plt.pause(0.03)
    t += 0.01

    
