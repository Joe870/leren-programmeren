# Robotarm bibliotheek inladen
from RobotArm import RobotArm

# De robotarm opstarten in een bepaald level, bijvoorbeeld 'exercise 1'
robotArm = RobotArm() 
RobotArm = robotArm.randomLevel(1,7)

# Jouw python instructies zet je vanaf hier:
teller = 1
move = True
while move == True:
    robotArm.grab()
    color = robotArm.scan()
    if color == '':
        move = False
    else:
        for blockright in range(teller):
            robotArm.moveRight()
        robotArm.drop()
        for blockleft in range(teller):
            robotArm.moveLeft()
        teller += 1



# Na jouw code wachten tot het sluiten van de window:
robotArm.wait() 