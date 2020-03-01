def interleave(a, b):
    # t = list(zip(a, b))
    # t1 = [''.join(pair) for pair in t]
    # t2 = ''.join(t1)
    # print(t2)

    return print(''.join([''.join(pair) for pair in list(zip(a, b))]))


interleave('aaa', 'zzz')
