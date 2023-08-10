# def selection_sort(numbers):
#     newnum_sort=[]
#     for i in numbers:
#         min_idx = i
#         newnum_sort.append(min_idx)
#         for j in newnum_sort:
#             if j < min_idx:
#                 min_idx = j
#                 newnum_sort.append(min_idx)
#     return newnum_sort

# numbers = [17, 5, 9, 12, 2]
# print(selection_sort(numbers))

# def bubble_sort(lst):
#     n = len(lst) - 1
#     for _ in range(n):
#         swapped = False
#         for x in range(n):
#             if lst[x] > lst[x + 1]:
#                 lst[x], lst[x + 1] = lst[x + 1], lst[x]
#                 swapped = True
#         if not swapped:
#             break
#     return lst

# print(bubble_sort([17, 5, 9, 12, 2]))

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result

def fasted_sort(lst):
    # Base case
    if lst == [] or lst is None:
        return lst

    midpoint = len(lst) // 2
    left = lst[:midpoint]
    right = lst[midpoint:]

    sorted_left = fasted_sort(left)
    sorted_right = fasted_sort(right)

    merged_sorted = merge(sorted_left, sorted_right)
    return merged_sorted

print("Sorted List:", fasted_sort([34, 68, -10, 1, -2, 10, 10]))



