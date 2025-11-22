# Remove duplicates from a list using set
nums = [1, 2, 2, 3, 4, 4]
unique_nums = list(set(nums))
if len(unique_nums) == 4:
    print(unique_nums)
else:
    print("Unexpected number of unique elements.")