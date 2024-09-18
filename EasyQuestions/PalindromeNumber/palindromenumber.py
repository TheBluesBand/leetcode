class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False

        x = list(str(x))
        compare = x

        for i in range(len(x)):
            if x[i] != x[-i-1]:
                return False

        return True