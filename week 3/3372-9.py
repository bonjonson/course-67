def modify_list(lst):
    lst_len = len(lst) #переменная хранящая длину списка
    cnt = 0 #переменная счетчик
    while cnt < lst_len:
        if lst[cnt] % 2 == 0:
            lst[cnt] = lst[cnt] // 2
            cnt += 1
        else:
            lst[cnt] = 'z'
            cnt += 1
    while 'z' in lst:
        lst.remove('z')