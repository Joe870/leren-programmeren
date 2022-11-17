# Robotarm bibliotheek inladen
from RobotArm import RobotArm

# De robotarm opstarten in een bepaald level, bijvoorbeeld 'exercise 1'
robotArm = RobotArm() 
RobotArm = robotArm.randomLevel(1,7)

# Jouw python instructies zet je vanaf hier:
robotArm.grab()
for stapel in range(7):
    color = robotArm.scan()
    if color != '':
        for blockright in range(stapel + 1):
            robotArm.moveRight()
        robotArm.drop()
        for blockleft in range(stapel + 1):
            robotArm.moveLeft()
        robotArm.grab()


# Na jouw code wachten tot het sluiten van de window:
robotArm.wait() 