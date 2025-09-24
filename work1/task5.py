def map_nums():
    A = [1,    2,   3,   4,   2,   1,   3,   4,   5,   6,   5,   4,   3,   2]
    B = ['a', 'b', 'c', 'c', 'c', 'b', 'a', 'c', 'a', 'a', 'b', 'c', 'b', 'a']
    result = {}
    for a, b in zip(A, B):
        result[b] = result.get(b, 0) + a
    print(result)

map_nums()