class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = 0
        digits[-1] += 1
        for i in range(len(digits) - 1, -1, -1):
            temp = digits[i] + carry
            carry = temp // 10
            digits[i] = temp % 10
        if carry == 1:
            return [1] + digits
        return digits
        
