def trap(height):
    if not height:
        return 0
    left = 0
    right = len(height) - 1
    left_max = right_max = 0
    res = 0
    while left < right:
        if height[left] < height[right]:
            if height[left] >= left_max:
                left_max = height[left]
            else:
                res += left_max - height[left]
            left += 1
        else:
            if height[right] >= right_max:
                right_max = height[right]
            else:
                res += right_max - height[right]
            right -= 1
    return res

# 测试示例1
height1 = [0,1,0,2,1,0,1,3,2,1,2,1]
print(f"示例1输出：{trap(height1)}")  # 输出 6

# 测试示例2
height2 = [4,2,0,3,2,5]
print(f"示例2输出：{trap(height2)}")  # 输出 9