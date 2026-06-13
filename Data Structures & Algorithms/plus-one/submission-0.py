class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = True
        for i in range(1, len(digits) + 1):
            carry = False
            if digits[i*-1] == 9:
                digits[i*-1] = 0
                carry = True
            else:
                digits[i*-1] = digits[i*-1] + 1
                break
        if carry:
            digits.insert(0, 1)
        return digits