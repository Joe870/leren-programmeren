# Robotarm bibliotheek inladen
from RobotArm import RobotArm

# De robotarm opstarten in een bepaald level, bijvoorbeeld 'exercise 1'
RobotArm = RobotArm('exercise 12') 

# Jouw python instructies zet je vanaf hier:
RobotArm.speed = 2
blockleft = 0
color = RobotArm.scan()
for blocks in range(8):
    RobotArm.moveRight()
for stapels in range(9):
    RobotArm.grab()
    RobotArm.scan()
    if RobotArm.scan() == 'red':
        for blockright in range(stapels + 1):
            RobotArm.moveRight()
        RobotArm.drop()
        for blockleft in range(stapels + 1):
            RobotArm.moveLeft()
    else: RobotArm.drop()
    if stapels <8:
        RobotArm.moveLeft()

# Na jouw code wachten tot het sluiten van de window:
RobotArm.wait() 