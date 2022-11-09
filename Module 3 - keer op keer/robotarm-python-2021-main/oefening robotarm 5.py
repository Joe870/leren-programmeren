# Robotarm bibliotheek inladen
from RobotArm import RobotArm

# De robotarm opstarten in een bepaald level, bijvoorbeeld 'exercise 1'
RobotArm = RobotArm('exercise 5') 

# Jouw python instructies zet je vanaf hier:
for x in range(1,8):
    RobotArm.moveRight()
for x in range(1,9):
    RobotArm.grab()
    RobotArm.moveRight()
    RobotArm.drop()
    if x < 8:
        RobotArm.moveLeft()
        RobotArm.moveLeft()
# Na jouw code wachten tot het sluiten van de window:
RobotArm.wait() 
