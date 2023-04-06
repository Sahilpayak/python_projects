pyInstaller = True
values = ["python","python@123",3.7,pyInstaller,100,123,88,126]
val = [111,122,633,344,255]

print(values)
values.append("spyder")
print(values)
values.pop(1)
print(values)
values.remove(100)
print(values)
values.insert(1,"admin@123")
print(values)
val.sort()
print(val)
values.reverse()
print(values)
values.extend(val)
print(val)
print(values)

for x in values:
    print(x)

for y in val:
    print (y+11)
values.clear()
print(values)
