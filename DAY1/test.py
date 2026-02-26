def is_palindrome(s):
    """Check if a string is a palindrome."""
    cleaned = s.lower().replace(" ", "")
    return cleaned == cleaned[::-1]

# Test cases
print(is_palindrome("racecar"))  # True
print(is_palindrome("hello"))    # False
print(is_palindrome("A man a plan a canal Panama"))  # True