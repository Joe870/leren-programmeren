# Robotarm bibliotheek inladen
from RobotArm import RobotArm

# De robotarm opstarten in een bepaald level, bijvoorbeeld 'exercise 1'
RobotArm = RobotArm('exercise 6') 

# Jouw python instructies zet je vanaf hier:
RobotArm.moveRight()
for x in range(0,3):
    RobotArm.grab()
    RobotArm.moveLeft()
    RobotArm.drop()
    RobotArm.moveRight()
    RobotArm.grab()
    RobotArm.moveRight()
    RobotArm.drop()
    RobotArm.moveLeft()

# Na jouw code wachten tot het sluiten van de window:
RobotArm.wait() 
