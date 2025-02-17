# Problem: Masha and Beautiful Tree - https://codeforces.com/problemset/problem/1741/D


def mergeSort(left, right, leaf_parents):
    if left < right:
        mid = left + (right - left) // 2

        left_arr = mergeSort(left, mid, leaf_parents)
        right_arr = mergeSort(mid + 1, right, leaf_parents)

        if not left_arr or not right_arr:
            return 
        return merge(left_arr, right_arr)
    return leaf_parents[left]

def merge(left_arr, right_arr):
    if left_arr[-1] < right_arr[0]:
        return (left_arr[0], right_arr[-1])
    if left_arr[0] > right_arr[-1]:
        operations[0] += 1
        return (right_arr[0], left_arr[-1])
    

t = int(input())

for _ in range(t):
    m = int(input())
    perm = [int(x) for x in input().split()]

    if m == 1:
        print(0)
    elif m == 2:
        print(1 if perm[0] > perm[1] else 0)
    else:
        operations = [0]
        leaf_parents = []
        for i in range(0, len(perm), 2):
            first,second = perm[i],perm[i + 1]
            if second < first:
                first,second = second, first
                operations[0] += 1
            leaf_parents.append((first, second))

        if mergeSort(0, len(leaf_parents) - 1, leaf_parents):
            print(operations[0])
        else:
            print(-1)
        