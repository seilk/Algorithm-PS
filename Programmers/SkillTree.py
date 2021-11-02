
def solution(skill, skill_trees):
    ans = 0
    for skill_tree in skill_trees:
        flag = True
        skill_idx, idx = 0, 0
        while idx < len(skill) and skill_idx < len(skill_tree):
            if skill[idx] == skill_tree[skill_idx]:
                idx += 1
            elif skill_tree[skill_idx] in skill and skill[idx] != skill_tree[skill_idx]:
                flag = False
                break
            elif skill[idx] not in skill_tree:
                pass
            skill_idx += 1
        if flag:
            ans += 1
    return ans


print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))
