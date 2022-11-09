# Robotarm bibliotheek inladen
from RobotArm import RobotArm

# De robotarm opstarten in een bepaald level, bijvoorbeeld 'exercise 1'
RobotArm = RobotArm('exercise 4') 

# Jouw python instructies zet je vanaf hier:
for x in range(1,5):
    RobotArm.grab()
    RobotArm.moveRight()
    RobotArm.moveRight()
    RobotArm.drop()
    RobotArm.moveLeft()
    RobotArm.moveLeft()
RobotArm.grab()
RobotArm.moveRight()
RobotArm.drop()
for x in range(1,5): 
    RobotArm.moveRight()
    RobotArm.grab()
    RobotArm.moveLeft()
    RobotArm.drop()
    
# RobotArm.moveRight()
# RobotArm.grab()
# RobotArm.moveLeft()
# RobotArm.drop()
# RobotArm.moveRight()
# RobotArm.grab()
# RobotArm.moveLeft()
# RobotArm.drop()
# RobotArm.moveRight()
# RobotArm.grab()
# RobotArm.moveLeft()
# RobotArm.drop()
# RobotArm.moveRight()
# RobotArm.grab()
# RobotArm.moveLeft()
# RobotArm.drop()
# Na jouw code wachten tot het sluiten van de window:
RobotArm.wait() 