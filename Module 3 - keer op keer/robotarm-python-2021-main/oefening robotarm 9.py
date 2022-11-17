# Robotarm bibliotheek inladen
from RobotArm import RobotArm

# De robotarm opstarten in een bepaald level, bijvoorbeeld 'exercise 1'
RobotArm = RobotArm('exercise 9') 

# Jouw python instructies zet je vanaf hier:
RobotArm.speed = 2 
for stapel in range(4):
    for stapelblock in range(stapel + 1):
        RobotArm.grab()
        for block in range(5):
            RobotArm.moveRight()
        RobotArm.drop()
        for block in range(5):
            RobotArm.moveLeft()
    RobotArm.moveRight()


# Na jouw code wachten tot het sluiten van de window:
RobotArm.wait() 