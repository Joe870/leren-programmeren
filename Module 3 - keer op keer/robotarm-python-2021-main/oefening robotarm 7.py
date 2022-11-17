# Robotarm bibliotheek inladen
from RobotArm import RobotArm

# De robotarm opstarten in een bepaald level, bijvoorbeeld 'exercise 1'
RobotArm = RobotArm('exercise 7') 

# Jouw python instructies zet je vanaf hier:
RobotArm.speed = 2 
for stapel in range(5):
    for blok in range(6):
        RobotArm.moveRight()
        RobotArm.grab()
        RobotArm.moveLeft()
        RobotArm.drop()
    if stapel <4:
        RobotArm.moveRight()
        RobotArm.moveRight()

# Na jouw code wachten tot het sluiten van de window:
RobotArm.wait() 