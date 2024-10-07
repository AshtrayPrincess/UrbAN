# Неизменяемые и изменяемые объекты. Кортежи.

immutable_var = 1.0, 78547, "str"
print(immutable_var)
print(type(immutable_var))

# кортежи неизменны
# кортежи пддерживают только два вида операций: конкатенацию и умножение

mutablelist = [123,"palm",123.123]
mutablelist[0] = 1
mutablelist.append(321)
mutablelist.extend('trs')
print(mutablelist)


