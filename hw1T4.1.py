def find_one_local_min(arr):
    # 处理边界条件
    if len(arr) == 2:
        return arr[1]

    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2

        # 边界情况处理
        if mid == 0:
            if arr[mid] < arr[mid + 1]:
                return arr[mid]
            else:
                left = mid + 1
        elif mid == len(arr) - 1:
            if arr[mid] < arr[mid - 1]:
                return arr[mid]
            else:
                right = mid - 1
        else:
            # 找到局部最小值
            if arr[mid] < arr[mid - 1] and arr[mid] < arr[mid + 1]:
                return arr[mid]
            # 向左搜索
            elif arr[mid] > arr[mid - 1]:
                right = mid - 1
            # 向右搜索
            else:
                left = mid + 1
    return None


# 测试
arr = [5, 3, 4, 2, 1, 6, 7, 8]
print("一个局部最小值:", find_one_local_min(arr))