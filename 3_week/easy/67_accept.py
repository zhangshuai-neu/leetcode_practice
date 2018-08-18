class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        #将二进制字符串转化为10进制整数
        a_int=int(a,2)
        b_int=int(b,2)
        sum_int = a_int + b_int
        #将10进制整数，转化为二进制字符串，并去掉开头"0b"
        return bin(sum_int)[2:]
