#O(n) solution

def MoveZeros(nums):
    pointer_to_zero = 0
    run_pointer = 0
    while run_pointer < len(nums) and pointer_to_zero < len(nums):
        while(pointer_to_zero < len(nums) and nums[pointer_to_zero] != 0):
            pointer_to_zero += 1
        if nums[run_pointer] != 0:
            nums[run_pointer], nums[pointer_to_zero] = nums[pointer_to_zero], nums[run_pointer]
        run_pointer += 1
    return nums

nums = [0, 0, 0, 2, 0, 1, 3, 4, 0, 0]
print(MoveZeros(nums))
#[2, 1, 3, 4, 0, 0, 0, 0, 0, 0]
