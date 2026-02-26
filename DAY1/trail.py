def two_sum(arr, target):
    """
    Find two numbers in a sorted array that sum to target.
    Uses two-pointer technique.
    """
    left = 0
    right = len(arr) - 1
    
    while left < right:
        current_sum = arr[left] + arr[right]
        
        if current_sum == target:
            return [arr[left], arr[right]]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    
    return None


# Example usage
if __name__ == "__main__":
    numbers = [2, 7, 11, 15, 20]
    target = 22
    result = two_sum(numbers, target)
    print(f"Pair found: {result}")