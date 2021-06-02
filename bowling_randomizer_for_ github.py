#by C0d3Math
#made Wed 6/2/21

#set this up
import random as rnd

#sets of restrictions
balls = ["football","marble","regular ball"]
distances = [2.5,5,7.5,10,12.5,15,17.5,20]

#what is your ball
ball = rnd.choice(balls)
print("You will use a " + str(ball) + " as your ball.")

#what is your distance
distance = rnd.choice(distances)
print("You will bowl from " + str(distance) + " feet.")