def find_all_local_min(arr):
    local_mins = []
    n = len(arr)
    # 首尾元素不可能是局部最小值
    for i in range(1, n - 1):
        if arr[i] < arr[i - 1] and arr[i] < arr[i + 1]:
            local_mins.append(arr[i])
    return local_mins

# 测试
arr = [5, 3, 4, 2, 1, 6, 7, 8]
print("所有局部最小值:", find_all_local_min(arr))