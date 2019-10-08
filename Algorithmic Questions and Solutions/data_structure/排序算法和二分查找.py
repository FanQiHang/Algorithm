# -*-coding:utf-8 -*-
# @Time :2019/8/719:24
# @Author : liupengrui
# @FileName :order.py


# 冒泡排序
def bubble_sort(ls):
    for i in range(len(ls)):
        for j in range(1, len(ls) - i):
            if ls[j - 1] > ls[j]:
                ls[j - 1], ls[j] = ls[j], ls[j - 1]
    return ls


# 快速排序，利用分治思想
def quicksort(ls, p, r):
    if p < r:
        q = partion(ls, p, r)
        quicksort(ls, p, q - 1)
        quicksort(ls, q + 1, r)


def partion(ls, p, r):
    pivotkey = ls[p]
    while p < r:
        while p < r and ls[r] >= pivotkey:
            r = r - 1
        ls[p] = ls[r]
        while p < r and ls[p] <= pivotkey:
            p = p + 1
        ls[r] = ls[p]
    ls[p] = pivotkey  # 关键一步，此时p==r
    return p


# 堆排序
def HeapSort(input_list):
    # 调整parent结点为大根堆
    def HeapAdjust(input_list, parent, length):  # parent 表示最后一个非终端结点的下标

        temp = input_list[parent]
        lchild = 2 * parent + 1

        while lchild < length:
            if lchild + 1 < length and input_list[lchild] < input_list[lchild + 1]:
                lchild += 1  # 如果左孩子的值比右孩子小，则右孩子和父结点比较

            if temp > input_list[lchild]:  # 如果比自己孩子大，则跳出循环，继续执行下一个结点
                break

            input_list[parent] = input_list[lchild]  # 将子结点的值赋值给父结点

            # 继续往下走
            parent = lchild  # 更新父结点的下标
            lchild = 2 * lchild + 1

        # 不继续往下走了
        input_list[parent] = temp

    if input_list == []:
        return []
    sorted_list = input_list
    length = len(sorted_list)

    # 最后一个结点的下标为length//2-1
    # 建立初始大根堆
    for i in range(0, length // 2)[::-1]:  # 倒序
        HeapAdjust(sorted_list, i, length)
    # 交换堆顶元素和最后一个元素
    for j in range(1, length)[::-1]:
        # 把堆顶元素即第一大的元素与最后一个元素互换位置
        sorted_list[j], sorted_list[0] = sorted_list[0], sorted_list[j]
        # 换完位置之后将剩余的元素重新调整成大根堆
        HeapAdjust(sorted_list, 0, j)  # j表示长度，j下标对应每一次的最大值
        print(sorted_list)
    return sorted_list


def binary_search(ls, key):
    quicksort(ls, 0, len(ls) - 1)
    low = 0
    high = len(ls) - 1
    while low < high:
        mid = (low + high) // 2
        if key == ls[mid]:
            return mid
        elif key > ls[mid]:
            low = mid + 1
        else:
            high = mid - 1


if __name__ == '__main__':
    ls = [2, 4, 3, 5, 1]
    mm = bubble_sort(ls)

    list1 = [2, 8, 7, 1, 3, 5, 6, 4]
    # quicksort(list1, 0, len(list1) - 1)

    print(binary_search(list1, 6))

    input_list = [50, 123, 543, 187, 49, 30, 0, 2, 11, 100]
    print("input_list:")
    print(input_list)
    sorted_list = HeapSort(input_list)
    print("sorted_list:")
    print(input_list)
