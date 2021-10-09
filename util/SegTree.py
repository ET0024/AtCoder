class SegTreeMin:
    """
    以下のクエリを処理する
    1.update:  i番目の値をxに更新する
    2.get_min: 区間[l, r)の最小値を得る
    """

    def __init__(self, n, INF):
        """
        :param n: 要素数
        :param INF: 初期値（入りうる要素より十分に大きな数）
        """
        self.n = n
        n2 = 1 << (n - 1).bit_length()
        self.offset = n2
        self.tree = [INF] * (n2 << 1)
        self.INF = INF

    def update(self, i, x):
        """
        i番目の値をxに更新
        :param i: index(0-indexed)
        :param x: update value
        """
        i += self.offset
        self.tree[i] = x
        while i > 1:
            y = self.tree[i ^ 1]
            if y <= x:
                break
            i >>= 1
            self.tree[i] = x

    def get_min(self, a, b):
        """
        [a, b)の最小値を得る
        :param a: index(0-indexed)
        :param b: index(0-indexed)
        """
        result = self.INF

        l = a + self.offset
        r = b + self.offset
        while l < r:
            if r & 1:
                result = min(result, self.tree[r - 1])
            if l & 1:
                result = min(result, self.tree[l])
                l += 1
            l >>= 1
            r >>= 1

        return result

    def __str__(self):
        return ''.join(str(self.tree[self.offset:self.offset + self.n]))


# # usage
# s = SegTreeMin(10, 10 ** 7)
# for i in range(10):
#     s.update(i, 10 + i)
# print(s)
# print(s.get_min(0, 3))
# print(s.get_min(1, 4))
# print(s.get_min(2, 5))
#
# s.update(3, 3)
#
# print(s)
# print(s.get_min(0, 3))
# print(s.get_min(1, 4))
# print(s.get_min(2, 5))
#
