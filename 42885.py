def solution(people, limit):
    lifeboat = 0

    people.sort()

    peopleLight = people[0:len(people) // 2]
    peopleHeavy = people[len(people) // 2:len(people)]
    peopleLight.reverse()

    while (len(peopleLight) or len(peopleHeavy)):
        sumWeight = 0

        if (len(peopleLight) == 0):
            if (len(peopleHeavy) == 1):
                lifeboat = lifeboat + 1
                break

            else:
                peopleLight = peopleHeavy[0:len(peopleHeavy) // 2]
                peopleHeavy = peopleHeavy[len(peopleHeavy) // 2:len(peopleHeavy)]

                peopleLight.reverse()

        elif (len(peopleHeavy) == 0):
            if (len(peopleLight) == 1):
                lifeboat = lifeboat + 1
                break

            else:
                peopleLight.reverse()

                peopleHeavy = peopleLight[len(peopleLight) // 2:len(peopleLight)]
                peopleLight = peopleLight[0:len(peopleLight) // 2]

                peopleLight.reverse()

        else:
            pL = peopleLight[-1]
            pH = peopleHeavy[-1]

            if (pL + pH <= limit):
                peopleLight.pop()
                peopleHeavy.pop()

            else:
                peopleHeavy.pop()

            lifeboat = lifeboat + 1

    return lifeboat
