import random

successNormal = 0
successSwitch = 0

for i in range(0, 10000):
    print('test ' + str(i))
    boxs = [False, False, False]

    giftIdx = random.randint(0, len(boxs) - 1)
    boxs[giftIdx] = True

    selectIdx = random.randint(0, len(boxs) - 1)
    if boxs[selectIdx]:
        successNormal = successNormal + 1

    for idx, box in enumerate(boxs):
        if selectIdx != idx and box is not True:
            boxs.pop(idx)
            if selectIdx > idx:
                selectIdx = selectIdx - 1
            break

    if selectIdx == 0:
        switchIdx = 1
    else:
        switchIdx = 0

    if boxs[switchIdx]:
        successSwitch = successSwitch + 1

    print(' giftIdx : ' + str(giftIdx) + ', selectIdx : ' + str(selectIdx) + ', switchIdx : ' + str(switchIdx))
    print(' successNormal : ' + str(successNormal))
    print(' successSwitch : ' + str(successSwitch))
