import random

#주의 : 정렬되지 않은 리스트에 쓰면 무한 루프에 빠짐.
#간단히 어떤 원소가 있는지 여부만 찾는 함수(있으면 True, 없으면 False 반환)
def binary_search(search_range, search_target):
    if len(search_range) ==1 and search_target == search_range[0]:
        return True
    if len(search_range) ==1 and search_target!= search_range[0]:#전부 다 돌았는데 찾는 값이 없는 경우
        return False
    if len(search_range) == 0: # 방어 코드, 입력 값 자체가 이상한 경우
        return False

    middle = len(search_range)//2 #둘로 나눈 몫
    if search_target == search_range[middle]:
        return True
    elif search_target > search_range[middle]:
        return binary_search(search_range[middle+1:], search_target)
    else:
        return binary_search(search_range[:middle-1], search_target)

test_list = random.sample(range(100), 10)
test_list.sort()
print(test_list)
print(binary_search(test_list, 10))