# Robotarm bibliotheek inladen
from RobotArm import RobotArm

# De robotarm opstarten in een bepaald level, bijvoorbeeld 'exercise 1'
RobotArm = RobotArm('exercise 2') 

# Jouw python instructies zet je vanaf hier:
RobotArm.grab() 
for x in range(1,10):
    RobotArm.moveRight() 
RobotArm.drop() 
for x in range(1,6):
    RobotArm.moveLeft()
RobotArm.grab()
for x in range(1,6):
    RobotArm.moveRight()
RobotArm.drop() 
for x in range(1,3):
    RobotArm.moveLeft()
RobotArm.grab()
for x in range(1,3):
    RobotArm.moveRight()
RobotArm.drop() 
# Na jouw code wachten tot het sluiten van de window:
RobotArm.wait() 