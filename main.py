lst = [1, 2, 3, 4, 5]
size = len(lst)
a = lst[:size//2:]
b = lst[size//2::]
#if a < b:      #тут вже не розумію як зробити щоб перший список був більшим
#    a = a + 1
print(a,b)