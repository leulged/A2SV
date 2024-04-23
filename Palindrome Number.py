class Solution:
    def isPalindrome(self, x: int) -> bool:
        int_string=str(x)
        reverse_string=int_string[::-1]
        if int_string==reverse_string:
            return True
        else:
            return False
