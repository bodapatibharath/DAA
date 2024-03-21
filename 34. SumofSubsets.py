def sum_of_subsets(nums, target):
    def backtrack(start, path, current_sum):
        if current_sum == target:
            result.append(path)
            return
        for i in range(start, len(nums)):
            if current_sum + nums[i] <= target:
                backtrack(i + 1, path + [nums[i]], current_sum + nums[i])

    nums.sort()
    result = []
    backtrack(0, [], 0)
    return result

nums = [2, 3, 7, 8, 10]
target = 10
print(sum_of_subsets(nums, target))
