class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        num1, num2 = num1[::-1], num2[::-1]
        carry, result = 0, ''
        for i in range(max(len(num1), len(num2))):
            a = 0 if i >= len(num1) else int(num1[i])
            b = 0 if i >= len(num2) else int(num2[i])
            result = result + str((carry + a + b) % 10)
            carry = (a + b + carry)//10
        if carry == 1:
            result = result + '1'
        return result[::-1]
