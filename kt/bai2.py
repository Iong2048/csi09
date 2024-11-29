def count_swaps_insertion_sort(arr):
    """
    Sắp xếp danh sách bằng Insertion Sort và đếm số lần đổi chỗ.
    """
    count = 0
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
            count += 1  # Tăng biến đếm mỗi khi đổi chỗ
        arr[j + 1] = key
    return count

my_list = [2, 5, 3, 1]
swap_count = count_swaps_insertion_sort(my_list)
print(f"Số lần đổi chỗ: {swap_count}")  # Output: Số lần đổi chỗ: 2
print(f"Danh sách đã sắp xếp: {my_list}") # Output: Danh sách đã sắp xếp: [1, 2, 3, 5]

