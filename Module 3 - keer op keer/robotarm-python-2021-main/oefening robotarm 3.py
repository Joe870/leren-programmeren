# Robotarm bibliotheek inladen
from RobotArm import RobotArm

# De robotarm opstarten in een bepaald level, bijvoorbeeld 'exercise 1'
RobotArm = RobotArm('exercise 3') 

# Jouw python instructies zet je vanaf hier:
for x in range(0,4):
    RobotArm.grab()
    RobotArm.moveRight()
    RobotArm.drop()
    RobotArm.moveLeft()
# Na jouw code wachten tot het sluiten van de window:
RobotArm.wait() 