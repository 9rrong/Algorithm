N = int(input())
nums = [int(input()) for _ in range(N)]

nums.sort()
res = 0

while nums:
    if nums[0] > 0:
        nums.sort(reverse = True)

    if len(nums) > 1:
        if nums[0] == 1 or nums[1] == 1:
            res += nums[0] + nums[1]
            nums.pop(0)
            nums.pop(0)
        elif nums[0] <= 0 and nums[1] <= 0:
            res += nums[0] * nums[1]
            nums.pop(0)
            nums.pop(0)
        elif nums[0] <= 0 < nums[1]:
            res += nums[0]
            nums.pop(0)
        elif nums[0] > 0 and nums[1] > 0:
            res += nums[0] * nums[1]
            nums.pop(0)
            nums.pop(0)
    else:
        res += nums[0]
        nums.pop(0)
        break

print(res)
