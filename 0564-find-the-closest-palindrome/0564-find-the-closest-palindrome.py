import math

class Solution:
    def nearestPalindromic(self, n: str) -> str:
        number = int(n)
        length = len(n)
        if length == 1:
            return str(number - 1)

        center = (length // 2) - 1 if length % 2 == 0 else length // 2
        first_half = n[:center + 1]

        def get_palindrome(first_half, even):
            return first_half + first_half[::-1] if even else first_half + first_half[:-1][::-1]

        candidates = [
            get_palindrome(first_half, length % 2 == 0),
            get_palindrome(str(int(first_half) + 1), length % 2 == 0),
            get_palindrome(str(int(first_half) - 1), length % 2 == 0),
            str(10 ** (length - 1) - 1),
            str(10 ** length + 1)
        ]

        candidates = [int(c) for c in candidates if int(c) != number]
        return str(min(candidates, key=lambda x: (abs(x - number), x)))