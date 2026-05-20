import heapq


def find_k_smallest_by_minheap(arr, k):
    # 建立最小堆（逐个插入方式）
    heap = []
    for num in arr:
        heapq.heappush(heap, num)

    # 提取k次最小值
    res = []
    for _ in range(k):
        res.append(heapq.heappop(heap))
    return res


# 测试
arr = [5, 4, 3, 2, 6, 1, 88, 33, 22, 107]
k = 3
print("最小堆法前k小：", find_k_smallest_by_minheap(arr, k))