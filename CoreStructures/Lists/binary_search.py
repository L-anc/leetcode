def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:

        mid = low + (high - low) // 2

        # Check if target is present at mid
        if arr[mid] == target:
            return mid

        # If target is greater, ignore left half
        elif arr[mid] < target:
            low = mid + 1

        # If target is smaller, ignore right half
        else:
            high = mid - 1

    # If we reach here, then the element
    # was not present
    return -1

print(binary_search([1, 2, 3, 4, 5], 3))  # Expected output: 2
print(binary_search([1, 2, 3, 4, 5], 6))  # Expected output: -1 (not found)
print(binary_search([], 1))  # Expected output: -1 (not found)
print(binary_search([1, 2, 3, 4, 5], 1))  # Expected output: 0
print(binary_search([1, 2, 4, 5], 2))  # Expected output: 1
print(binary_search([1, 2, 4, 5], 4))  # Expected output: 2


