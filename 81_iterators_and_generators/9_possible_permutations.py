def possible_permutations(nums):
    if len(nums) <= 1:
        yield nums
        return None
    for i in range(len(nums)):
        for x in possible_permutations(nums[:i]+nums[i+1:]):
            yield [nums[i]] + x

[print(n) for n in possible_permutations([1])]