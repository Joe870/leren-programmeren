# tafel = [1,2,3,4,5,6,7,8,9,10,11,12,13]
# for x in range(1, len(tafel) + 1):
#     for y in tafel:
#         uitkomst = x * y
#         print(f'tafel van {tafel}')
#         print(f' {x} * {y} = {uitkomst}')
for y in range(1,14):
    print('tafel van', y)
    for x in range(1,11):
        print(f' {x} *{y} = ', (x * y))

