def is_palindrome(s):
    # Base case: if the string has 0 or 1 characters, it's a palindrome
    if len(s) <= 1:
        return True
    # Check if the first and last characters are equal
    if s[0] != s[-1]:
        return False
    # Recursively check the substring without the first and last characters
    return is_palindrome(s[1:-1])

# Example usage
string = "radar"
if is_palindrome(string):
    print(f"{string} is a palindrome."
          ;
          )
else:
    print(f"{string} is not a palindrome.")
+-
