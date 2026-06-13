class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = True
        for i in range(len(digits) - 1, -1, -1):
            carry = False
            if digits[i] == 9:
                digits[i] = 0
                carry = True
            else:
                digits[i] = digits[i] + 1
                break
        if carry:
            digits.insert(0, 1)
        return digits