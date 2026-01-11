# marks = [3,5,6,9,32,12,34,22,45,21] 
# print(type(marks))
# print(marks[-6])
# print(marks[2:len(marks)])
# print(marks[0:10:2])

r = [3,5,7,2,32,54,2]
# r.append(8)
# r.sort()
# r.sort(reverse=True)
# r.reverse()
# print(r.index(54))
# print(r.count(54))
# print(r.insert(1 , 100))


m = [800, 900, 1000]
r.extend(m)
print(r)
print(type(r))

r.remove(32)
print(r)

for i in r:
    print(i)