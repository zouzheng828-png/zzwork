def find_k_smallest_by_sort(arr, k):
    # 排序
    arr_sorted = sorted(arr)
    # 取前k个
    return arr_sorted[:k]

# 测试
arr = [5,4,3,2,6,1,88,33,22,107]
k = 3
print("排序法前k小：", find_k_smallest_by_sort(arr, k))