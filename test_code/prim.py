# -- coding: UTF-8 --
def prim(adj):
    return 0


if __name__ == '__main__':
    T = int(input().strip())
    for iteration in range(T):
        n, m = map(int, input().split())
        adjacent = [[1]*n for _ in range(n)]
        for i in range(m):
            x, y = map(int, input().split())
            adjacent[x-1][y-1] = 2
        print("Case #%d: %d\n" % (iteration + 1, prim(adjacent)))
        