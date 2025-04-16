def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half, right_half = arr[:mid], arr[mid:]
        merge_sort(left_half)
        merge_sort(right_half)
        
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            arr[k] = left_half[i] if left_half[i] < right_half[j] else right_half[j]
            i, j = (i + 1, j) if left_half[i] < right_half[j] else (i, j + 1)
            k += 1
        
        arr[k:] = left_half[i:] or right_half[j:]

def merge_and_sort_lists(list1, list2):
    merged_list = list1 + list2
    merge_sort(merged_list)
    return merged_list

# Example usage:
list1 = [3, 1, 4, 5]
list2 = [2, 8, 6, 7]
print("Sorted Merged List:", merge_and_sort_lists(list1, list2))
