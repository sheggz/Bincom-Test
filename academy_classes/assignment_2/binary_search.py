def rec_binary_search(list, target, left, right):
    

    if left > right:
        return -1  # Base case: Target not found
    
    mid = left + (right - left) // 2  # Avoids potential overflow
    
    if list[mid] == target:
        return mid  # Base case: Target found
    elif list[mid] < target:
        return rec_binary_search(list, target, mid + 1, right)  # Search in right half
    else:
        return rec_binary_search(list, target, left, mid - 1)  # Search in left half
    

print(rec_binary_search([6,0,7,5,1,9], 1, 0 , 5))