from collections import deque


def solution(skill, skill_trees):
    availSkillTree = 0

    skillSet = set(skill)

    for skills in skill_trees:
        skillDeque = deque(skill)

        flag = True

        for s in skills:
            if (len(skillDeque) == 0):
                break

            if (s in skillSet):
                top = skillDeque.popleft()

                if (s != top):
                    flag = False

                    break

        if (flag):
            availSkillTree += 1

    return availSkillTree
