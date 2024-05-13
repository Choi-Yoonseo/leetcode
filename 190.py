class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for _ in range(32):
            lsb = n & 1
            res = res << 1
            res = res | lsb
            n = n >> 1
        return res