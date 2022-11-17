# Robotarm bibliotheek inladen
from RobotArm import RobotArm

# De robotarm opstarten in een bepaald level, bijvoorbeeld 'exercise 1'
RobotArm = RobotArm('exercise 10') 

# Jouw python instructies zet je vanaf hier:
RobotArm.speed = 2
blockrechts = 10
blocklinks = 9
RobotArm.grab()
for stapel in range(5):
    for stapelblock in range(1):
        for blockrechts in range(blockrechts - 1):
            RobotArm.moveRight()
        RobotArm.drop()
        for blocklinks in range(blocklinks - 1):
            RobotArm.moveLeft()
    if stapel <4:
        RobotArm.grab()


# Na jouw code wachten tot het sluiten van de window:
RobotArm.wait() 
