from math import *

class Ball(object):
	xPos = 0.0
	yPos = 0.0
	xVel = 0.0
	yVel = 0.0
	xAcc = 0.0
	yAcc = 0.0
	mass = 0.0

	def applyForce(self, force, time):
		'''
		force: a force object being applied constantly over the time
		time: a float defining when we are finding the position
		'''
		self.xPos += self.xVel * time + 0.5 * (force.xForce)/self.mass * time**2.0
		self.yPos += self.yVel * time + 0.5 * (force.yForce)/self.mass * time**2.0
		self.xVel += force.xForce/self.mass * time
		self.yVel += force.yForce/self.mass * time

	def __str__(self):
		return "Pos:(" + str(self.xPos) + ", " + str(self.yPos) + ")"

class Force(object):
	xForce = 0.0
	yForce = 0.0

	def defForce(self, amount, direction):
		'''
		force: float
		direction: angle in radians
		'''
		self.xForce = cos(direction) * amount
		self.yForce = sin(direction) * amount

	def convertAngle(self, degrees):
		'''
		degrees: a float
		return: radians
		'''
		return degrees * pi / 180.0

f = Force();
f.defForce(1.0, 0.0);
b = Ball();
b.mass = 1.0;
b.applyForce(f, 10.0);	
print b