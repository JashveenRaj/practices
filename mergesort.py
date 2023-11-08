def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # Split the array into two halves
    middle = len(arr) // 2
    left_half = arr[:middle]
    right_half = arr[middle:]

    # Recursively sort each half
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # Merge the sorted halves
    return merge(left_half, right_half)

def merge(left, right):
    result = []
    left_idx, right_idx = 0, 0

    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1

    # Append any remaining elements from both lists
    result.extend(left[left_idx:])
    result.extend(right[right_idx:])

    return result

# Example usage:
arr = [12, 11, 13, 5, 6, 7,5,35,3,4,1,4,96,3,4]
sorted_arr = merge_sort(arr)
print("Sorted array:", sorted_arr)
