#не нашел метода обмена значений, не понял как применить input
a = [123, 5.5, 'text', False, [12468898]]

b = a[0]
c = a[1]
a.insert(1, b)
a.insert(0, c)
a.pop(2)
a.pop(2)

b = a[2]
c = a[3]
a.insert(2,c)
a.insert(3, b)
a.pop(4)
a.pop(4)

print(a)


