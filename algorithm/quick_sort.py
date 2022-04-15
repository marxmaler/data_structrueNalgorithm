import random

def qsort(target_list):
    if len(target_list) <=1:
        return target_list
    left, right = list(), list()
    pivot = target_list[0]

    for i in range(1, len(target_list)):
        if pivot > target_list[i]:
            left.append(target_list[i])
        else: #pivot보다 같거나 큰 경우
            right.append(target_list[i])
    return qsort(left) + [pivot] + qsort(right) #그냥 pivot을 리스트([])로 안만들고 그대로 더하면 리스트와 숫자를 더하는 것이므로 에러가 발생한다.

def qsort_with_comprehension(target_list):
    if len(target_list) <=1:
        return target_list
    pivot = target_list[0]

    left = [item for item in target_list[1:] if pivot > item]
    right = [item for item in target_list[1:] if pivot <= item]
    return qsort_with_comprehension(left) + [pivot] + qsort_with_comprehension(right)

test_list = random.sample(range(100), 10)
print(qsort(test_list))
