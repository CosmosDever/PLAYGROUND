def find_triplets(nums):
    nums.sort()
    return [sorted([nums[i], nums[j], nums[k]]) for i in range(len(nums) - 2) for j in range(i + 1, len(nums) - 1) for k in range(j + 1, len(nums)) if nums[i] + nums[j] + nums[k] == 0 and (i == 0 or nums[i] != nums[i-1]) and (j == i + 1 or nums[j] != nums[j-1]) and (k == j + 1 or nums[k] != nums[k-1])]

input_list = [-2, -1, 0, 1, 2, 3, 4, 5, 6, 7]
result = find_triplets(input_list)
print(result)  # Output: [[-2, -1, 3], [-2, 0, 2], [-1, 0, 1]]



