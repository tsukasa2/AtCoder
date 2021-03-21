## ここから引用
class SegTree:
    """
    init(init_val, ide_ele): 配列init_valで初期化 O(N)
    update(k, x): k番目の値をxに更新 O(logN)
    query(l, r): 区間[l, r)をsegfuncしたものを返す O(logN)
    """
    def __init__(self, init_val, segfunc, ide_ele):
        """
        init_val: 配列の初期値
        segfunc: 区間にしたい操作
        ide_ele: 単位元
        n: 要素数
        num: n以上の最小の2のべき乗
        tree: セグメント木(1-index)
        """
        n = len(init_val)
        self.segfunc = segfunc
        self.ide_ele = ide_ele
        self.num = 1 << (n - 1).bit_length()
        self.tree = [ide_ele] * 2 * self.num
        # 配列の値を葉にセット
        for i in range(n):
            self.tree[self.num + i] = init_val[i]
        # 構築していく
        for i in range(self.num - 1, 0, -1):
            self.tree[i] = self.segfunc(self.tree[2 * i], self.tree[2 * i + 1])

    def update(self, k, x):
        """
        k番目の値をxに更新
        k: index(0-index)
        x: update value
        """
        k += self.num
        self.tree[k] = x
        while k > 1:
            self.tree[k >> 1] = self.segfunc(self.tree[k], self.tree[k ^ 1])
            k >>= 1

    def query(self, l, r):
        """
        [l, r)のsegfuncしたものを得る
        l: index(0-index)
        r: index(0-index)
        """
        res = self.ide_ele

        l += self.num
        r += self.num
        while l < r:
            if l & 1:
                res = self.segfunc(res, self.tree[l])
                l += 1
            if r & 1:
                res = self.segfunc(res, self.tree[r - 1])
            l >>= 1
            r >>= 1
        return res
## ここまで引用

from collections import Counter

N, M = map( int, input().split() )
A = list( map( int, input().split() ) )

INF = 2 * 10 ** 6
C = Counter()
st = SegTree( [ i for i in range( N ) ], min, N )

# i = 0のときのmexを求めansとする
for i in range( M ):
    a = A[ i ]
    C[ a ] += 1
    st.update( a, INF )

ans = st.query( 0, N )

# i = 1以降はseg木を更新してmexを求める
for i in range( 1, N - M + 1 ):
    a_del = A[ i - 1 ]      # 削除する値
    C[ a_del ] -= 1
    a_add = A[ i + M - 1 ]  # 追加する値
    C[ a_add ] += 1

    if C[ a_del ] == 0:
        # a_delが存在しなくなっていれば
        st.update( a_del, a_del )
    
    if C[ a_add ] == 1:
        # a_addがもともとは存在していなければ
        st.update( a_add, INF )
    
    ans = min( ans, st.query( 0, N ) )

print( ans )