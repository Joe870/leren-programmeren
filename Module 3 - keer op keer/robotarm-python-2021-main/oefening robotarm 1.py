# Robotarm bibliotheek inladen
from RobotArm import RobotArm

# De robotarm opstarten in een bepaald level, bijvoorbeeld 'exercise 1'
RobotArm = RobotArm('exercise 1') 

# Jouw python instructies zet je vanaf hier:
RobotArm.moveRight()
RobotArm.grab()
RobotArm.moveLeft()
RobotArm.drop()
# RobotArm.operate
# Na jouw code wachten tot het sluiten van de window:
RobotArm.wait() 
