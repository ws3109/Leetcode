class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        result = "1"
        for i in range(1, n):
            result = result + '*'
            temp = ""
            count = 1
            for i in range(1, len(result)):
                if result[i] == result[i-1]:
                    count += 1
                else:
                    temp += str(count) + result[i-1]
                    count = 1
            result = temp
        return result
