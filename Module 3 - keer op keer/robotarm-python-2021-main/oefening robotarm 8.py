# Robotarm bibliotheek inladen
from RobotArm import RobotArm

# De robotarm opstarten in een bepaald level, bijvoorbeeld 'exercise 1'
RobotArm = RobotArm('exercise 8') 

# Jouw python instructies zet je vanaf hier:
RobotArm.speed =2 

RobotArm.moveRight()
RobotArm.grab()
for stapel in range(7):
    for block in range(8):
        RobotArm.moveRight()
    RobotArm.drop()
    for block in range(8):
        RobotArm.moveLeft()
    RobotArm.grab()

# Na jouw code wachten tot het sluiten van de window:
RobotArm.wait() 