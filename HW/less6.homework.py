def index_two(nums, target):
    num_map = {}
    for i, num in enumerate(nums):
        component = target - num
        if component in num_map:
            return [num_map[component], i]
        num_map[num] = i
    return []

nums = [2,7,11,15]
target = 9
print(index_two(nums, target))
