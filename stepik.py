def modify_list(l):
    l = [l[i] // 2 for i in range(len(l) - 1, -1, -1) if l[i] % 2 == 0]
    l.reverse()
    return l


print(modify_list([1, 2, 3, 4, 5, 6]))