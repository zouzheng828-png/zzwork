def asteroid_collision(asteroids):
    stack = []

    for num in asteroids:
        # 当前星球还存活
        alive = True

        # 碰撞条件：栈顶向右(+)，当前向左(-)，且当前星球存活
        while stack and stack[-1] > 0 and num < 0 and alive:
            top = stack[-1]
            abs_top = abs(top)
            abs_num = abs(num)

            if abs_top > abs_num:
                # 栈顶更大，当前星球消失
                alive = False
            elif abs_top < abs_num:
                # 当前星球更大，栈顶消失
                stack.pop()
            else:
                # 质量相等：正的保留，负的消失
                stack.pop()
                alive = False

        # 存活就入栈
        if alive:
            stack.append(num)

    return stack


# ------------------- 测试 -------------------
# 测试用例1
A1 = [-3, -6, 2, 8, 5, -8, 9, -2, 1]
print("输入1:", A1)
print("输出1:", asteroid_collision(A1))  # [-3, -6, 2, 8, 9, 1]

print("-" * 50)

# 测试用例2
A2 = [23, -8, 9, -3, -7, 9, -23, 22]
print("输入2:", A2)
print("输出2:", asteroid_collision(A2))  # [23, 22]